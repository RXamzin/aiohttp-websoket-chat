import os
from app.views.view import index, chat
from app.config import BASE_DIR

def set_up_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/ws', chat)
    app.router.add_static('/static', path=os.path.join(BASE_DIR, 'static'), name='static', append_version=True)