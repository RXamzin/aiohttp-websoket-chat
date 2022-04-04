import os
from aiohttp import web
from app.config import BASE_DIR
from app.routes import set_up_routes
import aiohttp_jinja2
import jinja2


def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.path.join(BASE_DIR, 'templates')))
    set_up_routes(app)
    return app
    