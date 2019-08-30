from app.core.domain.car_model import CarModel
from app.infrastructure.repositories.car_model import CarModelRepository


class CarModelService:
    def __init__(self):
        self.repository = CarModelRepository()

    async def list_all_models(self, filtr=None):
        return [CarModel.from_dict(cm) for cm in await self.repository.get_many(filtr)]
