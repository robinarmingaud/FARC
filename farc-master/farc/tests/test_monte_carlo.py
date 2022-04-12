import dataclasses

import numpy as np
import pytest

import farc.models
import farc.monte_carlo.models as mc_models
import farc.monte_carlo.sampleable


MODEL_CLASSES = [
    cls for cls in vars(farc.models).values()
    if dataclasses.is_dataclass(cls)
]


def test_type_annotations():
    # Check that there are appropriate type annotations for all of the model
    # classes in farc.models. Note that these must be statically defined in
    # farc.monte_carlo, rather than being dynamically generated, in order to
    # allow the type system to be able to see their definition without needing
    # runtime execution.
    missing = []
    for cls in MODEL_CLASSES:
        if not hasattr(farc.monte_carlo, cls.__name__):
            missing.append(cls.__name__)
            continue
        mc_cls = getattr(farc.monte_carlo, cls.__name__)
        assert issubclass(mc_cls, farc.monte_carlo.MCModelBase)

    if missing:
        msg = (
            'There are missing model implementations in farc.monte_carlo. '
            'The following definitions are needed:\n  ' +
            '\n  '.join([f'{model} = build_mc_model(farc.models.{model})' for model in missing])
        )
        pytest.fail(msg)


@pytest.fixture
def baseline_mc_model() -> farc.monte_carlo.ConcentrationModel:
    mc_model = farc.monte_carlo.ConcentrationModel(
        room=farc.monte_carlo.Room(volume=farc.monte_carlo.sampleable.Normal(75, 20)),
        ventilation=farc.monte_carlo.SlidingWindow(
            active=farc.models.PeriodicInterval(period=120, duration=120),
            inside_temp=farc.models.PiecewiseConstant((0., 24.), (293,)),
            outside_temp=farc.models.PiecewiseConstant((0., 24.), (283,)),
            window_height=1.6, opening_length=0.6,
        ),
        infected=farc.models.InfectedPopulation(
            number=1,
            virus=farc.models.Virus.types['SARS_CoV_2'],
            presence=farc.models.SpecificInterval(((0., 4.), (5., 8.))),
            mask=farc.models.Mask.types['No mask'],
            activity=farc.models.Activity.types['Light activity'],
            expiration=farc.models.Expiration.types['Breathing'],
            host_immunity=0.,
        ),
        evaporation_factor=0.3,
    )
    return mc_model


@pytest.fixture
def baseline_mc_exposure_model(baseline_mc_model) -> farc.monte_carlo.ExposureModel:
    return farc.monte_carlo.ExposureModel(
        baseline_mc_model,
        exposed=farc.models.Population(
            number=10,
            presence=baseline_mc_model.infected.presence,
            activity=baseline_mc_model.infected.activity,
            mask=baseline_mc_model.infected.mask,
            host_immunity=0.,
        )
    )


def test_build_concentration_model(baseline_mc_model: farc.monte_carlo.ConcentrationModel):
    model = baseline_mc_model.build_model(7)
    assert isinstance(model, farc.models.ConcentrationModel)
    assert isinstance(model.concentration(time=0.), float)
    conc = model.concentration(time=1.)
    assert isinstance(conc, np.ndarray)
    assert conc.shape == (7, )


def test_build_exposure_model(baseline_mc_exposure_model: farc.monte_carlo.ExposureModel):
    model = baseline_mc_exposure_model.build_model(7)
    assert isinstance(model, farc.models.ExposureModel)
    prob = model.deposited_exposure()
    assert isinstance(prob, np.ndarray)
    assert prob.shape == (7, )
