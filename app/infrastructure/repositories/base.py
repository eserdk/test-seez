from bson import ObjectId


class BaseRepository:
    collection = None

    def __init__(self):
        pass

    async def get_one(self, filtr: dict):
        return await self.collection.find_one(filtr)

    async def get_one_by_id(self, _id: ObjectId):
        return self.get_one({'_id': _id})

    async def get_many(self, filtr: dict = None):
        if filtr is None:
            filtr = {}
        return [c async for c in self.collection.find(filtr)]

    async def create(self, domain_obj):
        result = await self.collection.insert_one(domain_obj.to_dict())
        domain_obj._id = result.inserted_id

    async def delete(self, domain_obj):
        await self.collection.delete_one(domain_obj.to_dict())
