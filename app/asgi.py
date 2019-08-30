import asyncio

import uvloop
from aiohttp import web


def create_app(loop=None):
    asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
    if loop:
        asyncio.set_event_loop(loop)
    app = web.Application()
    from app.infrastructure import db
    from app.ui.api.routes import routes
    app.add_routes(routes)
    db.init_app(app)
    return app


def start():
    web.run_app(create_app())
