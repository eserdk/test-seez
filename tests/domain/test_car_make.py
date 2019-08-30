from app.core.domain.car_make import CarMake


def test_car_make_init():
    car_make = CarMake(name='Nissan', active=True)
    assert car_make.name == 'Nissan'
    assert car_make.active


def test_car_make_from_dict():
    car_make = CarMake.from_dict(dict(name='Toyota', active=False))
    assert car_make.name == 'Toyota'
    assert not car_make.active


def test_car_make_to_dict():
    car_make = CarMake(name='Infinity', active=True)
    car_make2 = car_make.to_dict()
    assert car_make2['name'] == 'Infinity'
    assert car_make2['active']
