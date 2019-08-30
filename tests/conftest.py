import asyncio

import pytest

from app.asgi import create_app

pytest_plugins = 'aiohttp.pytest_plugin'


@pytest.yield_fixture(scope='session')
def loop(request):
    l = asyncio.get_event_loop_policy().new_event_loop()
    yield l
    l.close()


@pytest.fixture()
async def cli(aiohttp_client):
    return await aiohttp_client(create_app())
