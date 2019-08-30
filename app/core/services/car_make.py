from app.core.domain.car_make import CarMake
from app.infrastructure.repositories.car_make import CarMakeRepository


class CarMakeService:
    def __init__(self):
        self.repository = CarMakeRepository()

    async def list_all_makes(self, filtr=None):
        return [CarMake.from_dict(cm) for cm in await self.repository.get_many(filtr)]
