import motor.motor_asyncio

from config import MONGODB_HOST, MONGODB_PORT

client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_HOST, MONGODB_PORT)
db = client.seez


def init_app(app):
    app['db'] = db
