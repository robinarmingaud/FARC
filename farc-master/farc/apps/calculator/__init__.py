# This module is part of CARA. Please see the repository at
# https://gitlab.cern.ch/cara/cara for details of the license and terms of use.

import asyncio
import concurrent.futures
import datetime
import base64
from email.policy import default
import functools
import html
import json
import os
from pathlib import Path
import traceback
import typing
import uuid
import zlib
import mysql.connector as database
import jinja2
import loky
from tornado.web import Application, RequestHandler, StaticFileHandler
import tornado.log

from . import markdown_tools
from . import model_generator
from .report_generator import ReportGenerator
from .user import AuthenticatedUser, AnonymousUser
from .DEFAULT_DATA import __version__, _DEFAULTS as d
import tornado

tornado.locale.set_default_locale("en")
#Need to set environment variables in docker container 
username = os.environ.get("db_username")
password = os.environ.get("db_psswd")

connection = database.connect(
    user=username,
    password=password,
    host="fl-ubu-212.flow-r.fr",
    database="flow_r")

cursor = connection.cursor(buffered=True)


class BaseRequestHandler(RequestHandler):
    async def prepare(self):
        template_environment = self.settings["template_environment"]
        template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
        _ = tornado.locale.get(self.locale.code).translate
        """Called at the beginning of a request before  `get`/`post`/etc."""
    
        # Read the secure cookie which exists if we are in an authenticated
        # context (though not if the farc webservice is running standalone).
        token_browser = self.get_cookie('USER_TOKEN') or 'null'

        try : 
            cursor.execute("SELECT prenom, email, nom  FROM utilisateurs WHERE token='"+token_browser+"' LIMIT 1")
            current_user = cursor.fetchone()
            if current_user :
                    self.current_user = AuthenticatedUser(
                    username=current_user[0],
                    email=current_user[1],
                    fullname=current_user[2],
                    )
            else :
                self.current_user = AnonymousUser()
            
        except database.Error as e:
            print(f"Error retrieving entry from database: {e}")
            self.current_user = AnonymousUser()

        language = self.get_cookie('language') or 'null'
        if language == "null" : 
            template_environment = self.settings["template_environment"]
            template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
            _ = tornado.locale.get(self.locale.code).translate
        else :
            template_environment = self.settings["template_environment"]
            template_environment.globals['_']=tornado.locale.get(language ).translate
            _ = tornado.locale.get(language ).translate

    def write_error(self, status_code: int, **kwargs) -> None:
        if not self.current_user.is_authenticated() :
            self.redirect('https://www.flow-r.fr/')
        else :
            language = self.get_cookie('language') or 'null'
            if language == "null" : 
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
                _ = tornado.locale.get(self.locale.code).translate
            else :
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(language ).translate
                _ = tornado.locale.get(language ).translate
            template = self.settings["template_environment"].get_template(
                "error_page.html.j2")

            error_id = uuid.uuid4()
            contents = (
                _('Unfortunately an error occurred when processing your request. Please let us know about this issue with as much detail as possible at') + ' ' + '<a href="mailto:Flow-R-dev@ingenica.fr">Flow-R-dev@ingenica.fr</a>, ' + _('reporting status code') + ' ' + f'{status_code}' +  ', ' + _('the error id of :') + ' ' + f'{error_id}' +  ' ' + _('and the time of the request')+ ' ' + f'{datetime.datetime.utcnow()}' +'.<br><br><br><br>')
            # Print the error to the log (and not to the browser!)
            if "exc_info" in kwargs:
                print(f"ERROR UUID {error_id}")
                print(traceback.format_exc())
            self.finish(template.render(
                user=self.current_user,
                calculator_prefix=self.settings["calculator_prefix"],
                active_page='Error',
                contents=contents,
                default = DEFAULT_DATA._DEFAULTS
            ))


class Missing404Handler(BaseRequestHandler):
    async def prepare(self):
        if not self.current_user.is_authenticated() :
            self.redirect('https://www.flow-r.fr/')
        else :
            template_environment = self.settings["template_environment"]
            template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
            _ = tornado.locale.get(self.locale.code).translate
            await super().prepare()
            language = self.get_cookie('language') or 'null'
            if language == "null" : 
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
                _ = tornado.locale.get(self.locale.code).translate
            else :
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(language ).translate
                _ = tornado.locale.get(language ).translate       
            self.set_status(404)
            template = self.settings["template_environment"].get_template(
                "error_page.html.j2")
            self.finish(template.render(
                user=self.current_user,
                calculator_prefix=self.settings["calculator_prefix"],
                active_page='Error',
                contents=_('Unfortunately the page you were looking for does not exist.')+'<br><br><br><br>'
            ))


class ConcentrationModel(BaseRequestHandler):
    async def post(self):
        if not self.current_user.is_authenticated() :
            self.redirect('https://www.flow-r.fr/')
        else :
            language = self.get_cookie('language') or 'null'
            if language == "null" : 
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
                _ = tornado.locale.get(self.locale.code).translate
                locale_code = tornado.locale.get(language )
            else :
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(language ).translate
                _ = tornado.locale.get(language ).translate    
                locale_code = tornado.locale.get(language )    
            requested_model_config = {
                name: self.get_argument(name) for name in self.request.arguments
            }
            if self.settings.get("debug", False):
                from pprint import pprint
                pprint(requested_model_config)
                start = datetime.datetime.now()

            try:
                form = model_generator.FormData.from_dict(requested_model_config, tornado.locale.get(self.locale.code))
            except Exception as err:
                if self.settings.get("debug", False):
                    import traceback
                    print(traceback.format_exc())
                response_json = {'code': 400, 'error': _('Your request was invalid') + f'{html.escape(str(err))}'}
                self.set_status(400)
                self.finish(json.dumps(response_json))
                return

            base_url = self.request.protocol + "://" + self.request.host
            report_generator: ReportGenerator = self.settings['report_generator']
            report_generator.set_locale(locale_code)
            executor = loky.get_reusable_executor(
                max_workers=self.settings['handler_worker_pool_size'],
                timeout=300,
            )
            report_task = executor.submit(
                report_generator.build_report, base_url, form,
                executor_factory=functools.partial(
                    concurrent.futures.ThreadPoolExecutor,
                    self.settings['report_generation_parallelism'],
                ),
            )
            report: str = await asyncio.wrap_future(report_task)
            self.finish(report)


class StaticModel(BaseRequestHandler):
    async def get(self):
        if not self.current_user.is_authenticated() :
            self.redirect('https://www.flow-r.fr/')
        else :
            language = self.get_cookie('language') or 'null'
            if language == "null" : 
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
                _ = tornado.locale.get(self.locale.code).translate
                locale_code = tornado.locale.get(language )
            else :
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(language).translate
                _ = tornado.locale.get(language ).translate    
                locale_code = tornado.locale.get(language ) 
            form = model_generator.FormData.from_dict(model_generator.baseline_raw_form_data())
            base_url = self.request.protocol + "://" + self.request.host
            report_generator: ReportGenerator = self.settings['report_generator']
            report_generator.set_locale(locale_code)
            executor = loky.get_reusable_executor(max_workers=self.settings['handler_worker_pool_size'])
            report_task = executor.submit(
                report_generator.build_report, base_url, form,
                executor_factory=functools.partial(
                    concurrent.futures.ThreadPoolExecutor,
                    self.settings['report_generation_parallelism'],
                ),
            )
            report: str = await asyncio.wrap_future(report_task)
            self.finish(report)


class LandingPage(BaseRequestHandler):
    def get(self):
        if not self.current_user.is_authenticated() :
            self.redirect('https://www.flow-r.fr/')
        else :
            template_environment = self.settings["template_environment"]
            template = self.settings["template_environment"].get_template(
                "index.html.j2")
            language = self.get_cookie('language') or 'null'
            if language == "null" : 
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
            else :
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(language ).translate
            report = template.render(
                user=self.current_user,
                calculator_prefix=self.settings["calculator_prefix"],
                text_blocks= markdown_tools.extract_rendered_markdown_blocks(template_environment.get_template('common_text.md.j2'))
            )
            self.finish(report)


class AboutPage(BaseRequestHandler):
    def get(self):
        if not self.current_user.is_authenticated() :
            self.redirect('https://www.flow-r.fr/')
        else :
            language = self.get_cookie('language') or 'null'
            if language == "null" : 
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
            else :
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(language ).translate

            template = template_environment.get_template("about.html.j2")
            report = template.render(
                user=self.current_user,
                calculator_prefix=self.settings["calculator_prefix"],
                active_page="about",
                text_blocks= markdown_tools.extract_rendered_markdown_blocks(template_environment.get_template('common_text.md.j2'))
            )
            self.finish(report)


class CalculatorForm(BaseRequestHandler):
    def get(self):
        if not self.current_user.is_authenticated() :
            self.redirect('https://www.flow-r.fr/')
        else :
            with open('farc/apps/static/js/form.js', 'r') as original: data = original.read().splitlines(True)
            javascript_out = "var js_default = JSON.parse('{}');".format(json.dumps(d))
            with open('farc/apps/static/js/form.js', 'w') as modified: modified.writelines([javascript_out + "\n"] + data[1:])
            language = self.get_cookie('language') or 'null'
            if language == "null" : 
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
            else :
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(language ).translate
            template = template_environment.get_template(
                "calculator.form.html.j2")
            report = template.render(
                user=self.current_user,
                xsrf_form_html=self.xsrf_form_html(),
                calculator_prefix=self.settings["calculator_prefix"],
                calculator_version=__version__,
                default = DEFAULT_DATA._DEFAULTS,
                ACTIVITY_TYPES = DEFAULT_DATA.ACTIVITY_TYPES,
                PLACEHOLDERS = DEFAULT_DATA.PLACEHOLDERS,
                TOOLTIPS = DEFAULT_DATA.TOOLTIPS,
                text_blocks= markdown_tools.extract_rendered_markdown_blocks(template_environment.get_template('common_text.md.j2')),
                MONTH_NAMES = DEFAULT_DATA.MONTH_NAMES
            )
            self.finish(report)


class CompressedCalculatorFormInputs(BaseRequestHandler):
    def get(self, compressed_args: str):
        if not self.current_user.is_authenticated() :
            self.redirect('https://www.flow-r.fr/')
        else :
            language = self.get_cookie('language') or 'null'
            if language == "null" : 
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
                _ = tornado.locale.get(self.locale.code).translate
            else :
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(language ).translate
                _ = tornado.locale.get(self.locale.code).translate

            # Convert a base64 zlib encoded shortened URL into a non compressed
            # URL, and redirect.
            try:
                args = zlib.decompress(base64.b64decode(compressed_args)).decode()
            except Exception as err:  # noqa
                self.set_status(400)
                return self.finish(_("Invalid calculator data: it seems incomplete. Was there an error copying & pasting the URL?"))
            self.redirect(f'{self.settings["calculator_prefix"]}?{args}')


class ReadmeHandler(BaseRequestHandler):
    def get(self):
        if not self.current_user.is_authenticated() :
            self.redirect('https://www.flow-r.fr/')
        else :
            language = self.get_cookie('language') or 'null'
            if language == "null" : 
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(self.locale.code).translate
            else :
                template_environment = self.settings["template_environment"]
                template_environment.globals['_']=tornado.locale.get(language ).translate
            template = template_environment.get_template("userguide.html.j2")
            readme = template.render(
                active_page="calculator/user-guide",
                user=self.current_user,
                calculator_prefix=self.settings["calculator_prefix"],
                text_blocks= markdown_tools.extract_rendered_markdown_blocks(template_environment.get_template('common_text.md.j2')),
            )
            self.finish(readme)



def make_app(
        debug: bool = False,
        calculator_prefix: str = '/calculator',
        theme_dir: typing.Optional[Path] = None,
) -> Application:
    static_dir = Path(__file__).absolute().parent.parent / 'static'
    calculator_static_dir = Path(__file__).absolute().parent / 'static'
    urls: typing.Any = [
        (r'/?', LandingPage),
        (r'/_c/(.*)', CompressedCalculatorFormInputs),
        (r'/about', AboutPage),
        (r'/static/(.*)', StaticFileHandler, {'path': static_dir}),
        (calculator_prefix + r'/?', CalculatorForm),
        (calculator_prefix + r'/report', ConcentrationModel),
        (calculator_prefix + r'/baseline-model/result', StaticModel),
        (calculator_prefix + r'/user-guide', ReadmeHandler),
        (calculator_prefix + r'/static/(.*)', StaticFileHandler, {'path': calculator_static_dir}),
    ]
    cara_templates = Path(__file__).parent.parent / "templates"
    calculator_templates = Path(__file__).parent / "templates"
    templates_directories = [cara_templates, calculator_templates]
    if theme_dir:
        templates_directories.insert(0, theme_dir)
    loader = jinja2.FileSystemLoader([str(path) for path in templates_directories])
    template_environment = jinja2.Environment(
        loader=loader,
        undefined=jinja2.StrictUndefined,  # fail when rendering any undefined template context variable
        autoescape=jinja2.select_autoescape(['html', 'xml'])
    )

    if debug:
        tornado.log.enable_pretty_logging()

    return Application(
        urls,
        debug=debug,
        calculator_prefix=calculator_prefix,
        template_environment=template_environment,
        default_handler_class=Missing404Handler,
        report_generator=ReportGenerator(loader, calculator_prefix),
        xsrf_cookies=True,
        # COOKIE_SECRET being undefined will result in no login information being
        # presented to the user.
        cookie_secret=os.environ.get('COOKIE_SECRET', '<undefined>'),

        # Process parallelism controls. There is a balance between serving a single report
        # requests quickly or serving multiple requests concurrently.
        # The defaults are: handle one report at a time, and allow parallelism
        # of that report generation. A value of ``None`` will result in the number of
        # processes being determined based on the number of CPUs. For some deployments,
        # such as on OpenShift this number does *not* reflect the real number of CPUs that
        # can be used, and it is recommended to specify these values explicitly (through
        # the environment variables).
        handler_worker_pool_size=(
            int(os.environ.get("HANDLER_WORKER_POOL_SIZE", 1)) or None
        ),
        report_generation_parallelism=(
            int(os.environ.get('REPORT_PARALLELISM', 0)) or None
        ),
    )
