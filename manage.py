from settings.settings import DevConfig
import flask
import app
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from flask import Flask
def run(api):
    """ function Which start the API
    args:
        api (flask_restful.Api): builded API
    Returns:
        None
    """
    api.run()

api , client = app.create_app(DevConfig)  # create application
if __name__ == "__main__":
    run(api)
