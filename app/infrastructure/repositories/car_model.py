from app.infrastructure.db import db
from app.infrastructure.repositories.base import BaseRepository


class CarModelRepository(BaseRepository):
    def __init__(self):
        super(CarModelRepository, self).__init__()
        self.collection = db.car_models
