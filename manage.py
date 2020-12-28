from settings.settings import DevConfig
from app import create_app
api , client = create_app(DevConfig)  # create application
if __name__ == "__main__":
    api.run()
