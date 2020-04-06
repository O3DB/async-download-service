from app.views import (
    index,
    archive,
)


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/archive/{archive_hash}/', archive)
