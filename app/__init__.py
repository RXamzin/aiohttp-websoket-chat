from app.config import BASE_DIR, Config
from app.routes import set_up_routes
from app.tools.db import get_db_engine, get_db_session

import os
import logging
from aiohttp import web
import aiohttp_jinja2
import jinja2


async def on_start_up(app):
    engine = get_db_engine(
        app.CONFIG.DB_URL
    )
    
    session = get_db_session(engine)

    app.db = session
    app.db_engine = engine
    

async def on_shutdown(app):
    
    await app.db.close()
    await app.db_engine.dispose()


def create_app():
    app = web.Application()
    app['WEBSOCKETS'] = set()
    app.CONFIG = Config
    app.on_startup.append(on_start_up)
    app.on_shutdown.append(on_shutdown)
    
    logging.basicConfig(level=logging.DEBUG)
    aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.path.join(BASE_DIR, 'templates')))
    
    set_up_routes(app)
    return app
