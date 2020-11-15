from settings.settings import DevConfig
import app


def run(api):
    """ function Which start the API
    args:
        api (flask_restful.Api): builded API
    Returns:
        None
    """
    api.run()


if __name__ == "__main__":
    api = app.create_app(DevConfig)  # create application
    run(api)  # start application
