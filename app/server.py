#!/usr/bin/env python3

from aiohttp import web
from app.settings import CONFIG
from app.routes import setup_routes
from app.middlewares import setup_middlewares
from app.utils.logger import get_logger
from app.utils.logger import get_logger, setup_logging


logger = get_logger(__name__)


async def init_app():
    setup_logging()
    app = web.Application()
    app['config'] = CONFIG()
    setup_routes(app)
    setup_middlewares(app)
    return app


def run_app(host=None, port=None):
    port = port or CONFIG.SERVICE_PORT
    app = init_app()
    web.run_app(app, host=host, port=port)


if __name__ == '__main__':
    run_app()