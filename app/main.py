#!/usr/bin/env python3

from aiohttp import web
from app.settings import CONFIG
from app.routes import setup_routes
from app.middlewares import setup_middlewares
from app.utils.logger import get_logger


logger = get_logger(__name__)


async def init_app():
    print('INIT APP')
    app = web.Application()
    app['config'] = CONFIG()
    setup_routes(app)
    setup_middlewares(app)
    return app


def run_app():
    print('RUN APP')
    app = init_app()
    web.run_app(app, host='127.0.0.1', port=CONFIG.SERVICE_PORT)


if __name__ == '__main__':
    run_app()