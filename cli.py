import click
import pytest


@click.group('cli')
def cli():
    pass


@cli.group('db')
def db():
    """
    DB-related commands.
    """
    pass


@db.command('seed')
def seed():
    """
    Seeds database with initial data in ./data/seed
    """
    from app.infrastructure.services.seed import seed_db
    from asyncio import get_event_loop
    print('Database seeding started. Please, wait.')
    loop = get_event_loop()
    loop.run_until_complete(seed_db())
    loop.close()
    print('Success!')


@cli.command('start')
def start():
    """
    Starts aiohttp server.
    """
    from app.asgi import start as start_app
    start_app()


@cli.command('test')
@click.option('-c', '--coverage/--no-coverage', default=False, help='Enable code coverage.')
def test(coverage=False):
    """
    Performs testing.
    """
    if coverage:
        pytest.main(['-s', 'tests', '--cov', 'app'])
    else:
        pytest.main(['-s', 'tests'])


if __name__ == '__main__':
    cli()
