from app.views.view import index

def set_up_routes(app):
    app.router.add_get('/', index)