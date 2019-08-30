from app.core.domain.car_model import CarModel


def test_car_model_init():
    car_model = CarModel(make_id=1, name='SomeModel', active=True)
    assert car_model.make_id == 1
    assert car_model.name == 'SomeModel'
    assert car_model.active


def test_car_model_from_dict():
    car_model = CarModel.from_dict(dict(make_id=1, name='SomeModel', active=True))
    assert car_model.make_id == 1
    assert car_model.name == 'SomeModel'
    assert car_model.active


def test_car_model_to_dict():
    car_model = CarModel(make_id=1, name='SomeModel', active=True)
    car_model2 = car_model.to_dict()
    assert car_model2['make_id'] == 1
    assert car_model2['name'] == 'SomeModel'
    assert car_model2['active']
