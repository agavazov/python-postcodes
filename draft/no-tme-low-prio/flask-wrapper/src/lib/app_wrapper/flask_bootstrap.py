from flask import Flask
from .action_wrapper import ActionWrapper


class FlaskBootstrap:
    app: Flask = None
    main_route: str = None

    def __init__(self, name: str = "__main__", main_route: str = "/"):
        self.app = Flask(name)
        self.main_route = main_route if main_route[0:1] == "/" else "/" + main_route

    def run(self):
        self.app.run()

    def add_route(self, endpoint: str = None, endpoint_name: str = None, handler=None):
        """Register new route.
        @todo write more info here and fill the data about the parameters

        Parameters
        ----------
        :param endpoint: str: the URL rule as string
        :param endpoint_name:
        :param handler:
        """

        self.app.add_url_rule(rule=self.prepend_main_route(endpoint),
                              endpoint=endpoint_name,
                              view_func=ActionWrapper(handler))

    def prepend_main_route(self, endpoint: str) -> str:
        return self.main_route + endpoint
