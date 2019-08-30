from app.core.domain.car import Car
from app.infrastructure.repositories.car import CarRepository


class CarService:
    def __init__(self):
        self.repository = CarRepository()

    async def list_all_cars(self, filtr=None):
        return [Car.from_dict(c) for c in await self.repository.get_many(filtr)]

    async def list_all_cars_full(self, filtr=None):
        return [Car.from_dict(c) for c in await self.repository.get_many_full(filtr)]

    async def create_new_car(self, *args, **kwargs):
        car = Car(*args, **kwargs)
        await self.repository.create(car)
        return car
