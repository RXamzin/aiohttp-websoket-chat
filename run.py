import os
from aiohttp import web
from app.config import BASE_DIR
import aiohttp_jinja2
import jinja2

app = web.Application()
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader(os.path.join(BASE_DIR, 'templates')))

if __name__ == '__main__':
    web.run_app(app)