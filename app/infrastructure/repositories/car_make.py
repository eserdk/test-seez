from app.infrastructure.db import db
from app.infrastructure.repositories.base import BaseRepository


class CarMakeRepository(BaseRepository):
    def __init__(self):
        super(CarMakeRepository, self).__init__()
        self.collection = db.car_makes
