import concurrent.futures
import base64
import dataclasses
from datetime import datetime
import io
import json
from turtle import update
import typing
import urllib
import zlib
import time as t

import jinja2
import numpy as np

from farc import models
from farc.apps.calculator import markdown_tools
from farc.apps.calculator.DEFAULT_DATA import LOCALE

from ... import monte_carlo as mc
from .model_generator import FormData, _DEFAULT_MC_SAMPLE_SIZE
from ... import dataclass_utils

from babel.support import Translations
import gettext
_ = gettext.gettext


def model_start_end(model: models.ExposureModel):
    t_start = min(model.exposed.presence.boundaries()[0][0],
                  model.concentration_model.infected.presence.boundaries()[0][0])
    t_end = max(model.exposed.presence.boundaries()[-1][1],
                model.concentration_model.infected.presence.boundaries()[-1][1])
    return t_start, t_end


def fill_big_gaps(array, gap_size):
    """
    Insert values into the given sorted list if there is a gap of more than ``gap_size``.
    All values in the given array are preserved, even if they are within the ``gap_size`` of one another.

    >>> fill_big_gaps([1, 2, 4], gap_size=0.75)
    [1, 1.75, 2, 2.75, 3.5, 4]

    """
    result = []
    if len(array) == 0:
        raise ValueError("Input array must be len > 0")

    last_value = array[0]
    for value in array:
        while value - last_value > gap_size + 1e-15:
            last_value = last_value + gap_size
            result.append(last_value)
        result.append(value)
        last_value = value
    return result


def non_temp_transition_times(model: models.ExposureModel):
    """
    Return the non-temperature (and PiecewiseConstant) based transition times.

    """

    def walk_model(model, name=""):
        # Extend walk_dataclass to handle lists of dataclasses
        # (e.g. in MultipleVentilation).
        for name, obj in dataclass_utils.walk_dataclass(model, name=name):
            if name.endswith('.ventilations') and isinstance(obj, (list, tuple)):
                for i, item in enumerate(obj):
                    fq_name_i = f'{name}[{i}]'
                    yield fq_name_i, item
                    if dataclasses.is_dataclass(item):
                        yield from dataclass_utils.walk_dataclass(item, name=fq_name_i)
            else:
                yield name, obj

    t_start, t_end = model_start_end(model)

    change_times = {t_start, t_end}
    for name, obj in walk_model(model, name="exposure"):
        if isinstance(obj, models.Interval):
            change_times |= obj.transition_times()

    # Only choose times that are in the range of the model (removes things
    # such as PeriodicIntervals, which extend beyond the model itself).
    return sorted(time for time in change_times if (t_start <= time <= t_end))


def interesting_times(model: models.ExposureModel, approx_n_pts=100) -> typing.List[float]:
    """
    Pick approximately ``approx_n_pts`` time points which are interesting for the
    given model.

    Initially the times are seeded by important state change times (excluding
    outside temperature), and the times are then subsequently expanded to ensure
    that the step size is at most ``(t_end - t_start) / approx_n_pts``.

    """
    times = non_temp_transition_times(model)

    # Expand the times list to ensure that we have a maximum gap size between
    # the key times.
    nice_times = fill_big_gaps(times, gap_size=(max(times) - min(times)) / approx_n_pts)
    return nice_times


def calculate_report_data(model: models.ExposureModel):
    times = interesting_times(model)

    concentrations = [
        np.array(model.concentration_model.concentration(float(time))).mean()
        for time in times
    ]
    highest_const = max(concentrations)
    prob = np.array(model.infection_probability()).mean()
    er = np.array(model.concentration_model.infected.emission_rate_when_present()).mean()
    exposed_occupants = model.exposed.number
    expected_new_cases = np.array(model.expected_new_cases()).mean()
    cumulative_doses = np.cumsum([
        np.array(model.deposited_exposure_between_bounds(float(time1), float(time2))).mean()
        for time1, time2 in zip(times[:-1], times[1:])
    ])

    return {
        "times": list(times),
        "exposed_presence_intervals": [list(interval) for interval in model.exposed.presence.boundaries()],
        "cumulative_doses": list(cumulative_doses),
        "concentrations": concentrations,
        "highest_const": highest_const,
        "prob_inf": prob,
        "emission_rate": er,
        "exposed_occupants": exposed_occupants,
        "expected_new_cases": expected_new_cases,
    }


def generate_permalink(base_url, calculator_prefix, form: FormData):
    form_dict = FormData.to_dict(form, strip_defaults=True)

    # Generate the calculator URL arguments that would be needed to re-create this
    # form.
    args = urllib.parse.urlencode(form_dict)

    # Then zlib compress + base64 encode the string. To be inverted by the
    # /_c/ endpoint.
    compressed_args = base64.b64encode(zlib.compress(args.encode())).decode()
    qr_url = f"{base_url}/_c/{compressed_args}"
    url = f"{base_url}{calculator_prefix}?{args}"

    return {
        'link': url,
        'shortened': qr_url,
    }


def _img2bytes(figure):
    # Draw the image
    img_data = io.BytesIO()
    figure.save(img_data, format='png', bbox_inches="tight")
    return img_data


def img2base64(img_data) -> str:
    img_data.seek(0)
    pic_hash = base64.b64encode(img_data.read()).decode('ascii')
    # A src suitable for a tag such as f'<img id="scenario_concentration_plot" src="{result}">.
    return f'data:image/png;base64,{pic_hash}'


def minutes_to_time(minutes: int) -> str:
    minute_string = str(minutes % 60)
    minute_string = "0" * (2 - len(minute_string)) + minute_string
    hour_string = str(minutes // 60)
    hour_string = "0" * (2 - len(hour_string)) + hour_string

    return f"{hour_string}:{minute_string}"


def readable_minutes(minutes: int) -> str:
    time = float(minutes)
    unit = " minute"
    if time % 60 == 0:
        time = minutes / 60
        unit = " hour"
    if time != 1:
        unit += "s"

    if time.is_integer():
        time_str = "{:0.0f}".format(time)
    else:
        time_str = "{0:.2f}".format(time)

    return time_str + unit


def non_zero_percentage(percentage: int) -> str:
    if percentage < 0.01:
        return "<0.01%"
    elif percentage < 1:
        return "{:0.2f}%".format(percentage)
    else:
        return "{:0.1f}%".format(percentage)


def manufacture_alternative_scenarios(form: FormData) -> typing.Dict[str, mc.ExposureModel]:
    scenarios = {}

    if form.biov_option == 1:
        base = 3 if form.mask_wearing_option =='mask_on' else 2
    else:
        base = 1 if form.mask_wearing_option =='mask_on' else 0
    

    alternatives = (
        (
            _(f'NO bio-ventilation and NO masks'),
            dataclass_utils.replace(form, mask_wearing_option='mask_off', biov_option=0),

        ),
        (
            _(f'NO bio-ventilation and') + f'{form.mask_type}' + _('masks with a') + f'{form.exposed_mask_wear_ratio}' + _('wear ratio for exposed people and a') + f'{form.infected_mask_wear_ratio}' + _('wear ratio for infected people'),
            dataclass_utils.replace(form, mask_wearing_option='mask_on', biov_option=0),

        ),
        (
            f'{form.biov_amount}' + _('m3/h bio-ventilation and NO masks'),
            dataclass_utils.replace(form, mask_wearing_option='mask_off', biov_option=1),

        ),
        (
            f'{form.biov_amount}' + _('m3/h bio-ventilation and') + f'{form.mask_type}' + _('masks with a') + f'{form.exposed_mask_wear_ratio}' + _('wear ratio for exposed people and a') + f'{form.infected_mask_wear_ratio}' +  _('wear ratio for infected people'),
            dataclass_utils.replace(form, mask_wearing_option='mask_on', biov_option=1),
            
        ),
    )

    

    scenarios[f'Base: {alternatives[base][0]}'] = alternatives[base][1].build_mc_model()
    for i in range(0,len(alternatives)):
        if i == base:
            continue
        scenarios[f'Alt_{i+1}: {alternatives[i][0]}'] = alternatives[i][1].build_mc_model()


    return scenarios



def scenario_statistics(mc_model: mc.ExposureModel, sample_times: np.ndarray):
    start = t.process_time()
    model = mc_model.build_model(size=_DEFAULT_MC_SAMPLE_SIZE)

    '''cumulative_doses = np.cumsum([
        np.array(model.deposited_exposure_between_bounds(float(time1), float(time2))).mean()
        for time1, time2 in zip(sample_times[:-1], sample_times[1:])
    ])'''

    cumulative_doses = [
        np.array(model.cumulative_deposited_exposure(float(time))).mean()
        for time in sample_times
    ]
    
    print(t.process_time() - start) 
    return {
        'probability_of_infection': np.mean(model.infection_probability()),
        'expected_new_cases': np.mean(model.expected_new_cases()),
        'concentrations': [
            np.mean(model.concentration_model.concentration(time))
            for time in sample_times
        ],
        'cumulative_doses': list(cumulative_doses),
        'cumulative_infection_probabilities': [
            np.mean(model.cumulative_infection_probability(time))
            for time in sample_times
        ],
    }


# _scenario_colors = ("green","blue","magenta","orange","#386cb0","#f0027f","#bf5b17","#666666",)
_scenario_colors = ('MidnightBlue', "MediumBlue","DarkCyan", 'Turquoise', "#386cb0","#f0027f","#bf5b17","#666666",)

def comparison_report(
        scenarios: typing.Dict[str, mc.ExposureModel],
        sample_times: typing.List[float],
        executor_factory: typing.Callable[[], concurrent.futures.Executor],
):
    statistics = {}
    colors = {}
    with executor_factory() as executor:
        results = executor.map(
            scenario_statistics,
            scenarios.values(),
            [sample_times] * len(scenarios),
            timeout=60,
        )    

    row: int = 0
    for (name, model), model_stats in zip(scenarios.items(), results):
        statistics[name] = model_stats
        colors[name] = _scenario_colors[row]
        row += 1
    return {
        'stats': statistics,
        'colors': colors,
    }


@dataclasses.dataclass
class ReportGenerator:
    jinja_loader: jinja2.BaseLoader
    calculator_prefix: str

    def build_report(
            self,
            base_url: str,
            form: FormData,
            executor_factory: typing.Callable[[], concurrent.futures.Executor],
    ) -> str:
        model = form.build_model()
        context = self.prepare_context(base_url, model, form, executor_factory=executor_factory)
        return self.render(context)

    def prepare_context(
            self,
            base_url: str,
            model: models.ExposureModel,
            form: FormData,
            executor_factory: typing.Callable[[], concurrent.futures.Executor],
    ) -> dict:
        
        now = datetime.utcnow().astimezone()
        time = now.strftime("%Y-%m-%d %H:%M:%S UTC")

        context = {
            'model': model,
            'form': form,
            'creation_date': time,
        }

        scenario_sample_times = interesting_times(model)

        context.update(calculate_report_data(model))
        alternative_scenarios = manufacture_alternative_scenarios(form)
        
        context['alternative_scenarios'] = comparison_report(
            alternative_scenarios, scenario_sample_times, executor_factory=executor_factory,
        )
        context['prob_inf'] = next(iter(next(iter(context['alternative_scenarios'].items()))[1].items()))[1]['probability_of_infection']
        context['expected_new_cases'] = next(iter(next(iter(context['alternative_scenarios'].items()))[1].items()))[1]['expected_new_cases']
        context['permalink'] = generate_permalink(base_url, self.calculator_prefix, form)
        context['calculator_prefix'] = self.calculator_prefix
        
        return context

    def _template_environment(self) -> jinja2.Environment:
        env = jinja2.Environment(
            loader=self.jinja_loader,
            undefined=jinja2.StrictUndefined,
            extensions=['jinja2.ext.i18n', 'jinja2.ext.autoescape'],
            autoescape=jinja2.select_autoescape(['html', 'xml'])
        )
        env.filters['non_zero_percentage'] = non_zero_percentage
        env.filters['readable_minutes'] = readable_minutes
        env.filters['minutes_to_time'] = minutes_to_time
        env.filters['float_format'] = "{0:.2f}".format
        env.filters['int_format'] = "{:0.0f}".format
        env.filters['JSONify'] = json.dumps
        translation = Translations.load('locale', LOCALE)
        env.install_gettext_translations(translation)
        env.globals.update(_ = _)
        env.globals['text_blocks'] = markdown_tools.extract_rendered_markdown_blocks(env.get_template('common_text.md.j2'))
        return env

    def render(self, context: dict) -> str:
        template = self._template_environment().get_template("calculator.report.html.j2")
        return template.render(**context)
