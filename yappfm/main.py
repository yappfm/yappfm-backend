import logging
from importlib.metadata import entry_points

from fastapi import FastAPI

from yappfm.config import settings
from yappfm.models import db

logger = logging.getLogger(__name__)


def load_modules(app=None):
    for ep in entry_points()["yappfm.modules"]:
        logger.info(f"Loading module: {ep.name}")
        mod = ep.load()
        if app:
            init_app = getattr(mod, "init_app", None)
            if init_app:
                init_app(app)


def get_app():
    """Main FastAPI ASGI application."""
    app = FastAPI(title="GINO FastAPI Demo")
    db.init_app(app)
    return app
