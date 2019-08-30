import pymongo

from app.infrastructure.db import db
from app.infrastructure.repositories.base import BaseRepository


class CarRepository(BaseRepository):
    def __init__(self):
        super(CarRepository, self).__init__()
        self.collection = db.cars

    async def get_many_full(self, filtr: dict = None):
        pipeline = [
            {'$match': filtr if filtr else {}},
            {
                '$lookup': {
                    'from': 'car_submodels',
                    'localField': 'submodel_id',
                    'foreignField': '_id',
                    'as': 'submodel'
                }
            },
            {'$unwind': '$submodel'},
            {
                '$lookup': {
                    'from': 'car_models',
                    'localField': 'submodel.model_id',
                    'foreignField': '_id',
                    'as': 'model'
                }
            },
            {'$unwind': '$model'},
            {
                '$lookup': {
                    'from': 'car_makes',
                    'localField': 'model.make_id',
                    'foreignField': '_id',
                    'as': 'make'
                }
            },
            {'$unwind': '$make'},
            {'$sort': {'updated_at': pymongo.DESCENDING}}
        ]
        return [doc async for doc in self.collection.aggregate(pipeline)]
