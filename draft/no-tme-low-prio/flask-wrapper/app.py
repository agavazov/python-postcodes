from src.lib.app_wrapper import FlaskBootstrap


def action():
    return "whatever"


app_wrapper = FlaskBootstrap(name=__name__, main_route="app-test")
app_wrapper.add_route(endpoint='/test', endpoint_name='home', handler=action)
app_wrapper.run()
