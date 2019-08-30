from app.core.domain.car_submodel import CarSubmodel
from app.infrastructure.repositories.car_submodel import CarSubmodelRepository


class CarSubmodelService:
    def __init__(self):
        self.repository = CarSubmodelRepository()

    async def list_all_submodels(self, filtr=None):
        return [CarSubmodel.from_dict(cm) for cm in await self.repository.get_many(filtr)]
