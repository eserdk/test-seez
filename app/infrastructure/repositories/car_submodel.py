from app.infrastructure.db import db
from app.infrastructure.repositories.base import BaseRepository


class CarSubmodelRepository(BaseRepository):
    def __init__(self):
        super(CarSubmodelRepository, self).__init__()
        self.collection = db.car_submodels
