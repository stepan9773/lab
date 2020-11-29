from settings.settings import DevConfig
import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


def run(api):
    """ function Which start the API
    args:
        api (flask_restful.Api): builded API
    Returns:
        None
    """
    api.run()


if __name__ == "__main__":
    api = app.create_app()  # create application
    #run(api)  # start application

    migrate = Migrate(api, app.db)
    maneger = Manager(api)
    maneger.add_command('db', MigrateCommand)
    maneger.run()
