import importlib

from starlette.config import Config

# Load environment from .env file in root path
config = Config(".env")


class Settings:
    """Dynamic load of settings using YAPPFM_SETTINGS_FILE to define the package for 
    settings.
    """

    def __init__(self):
        settings_file = config("YAPPFM_SETTINGS_FILE", default="yappfm.config.local")
        self.module = importlib.import_module(settings_file)

    def __getattr__(self, name):
        if hasattr(self.module, name):
            return getattr(self.module, name)


# Singleton instance for dynamic settings
settings = Settings()
