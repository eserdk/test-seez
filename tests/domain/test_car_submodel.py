from app.core.domain.car_submodel import CarSubmodel


def test_car_submodel_init():
    car_submodel = CarSubmodel(model_id=1, name='Submodel', active=True)
    assert car_submodel.model_id == 1
    assert car_submodel.name == 'Submodel'
    assert car_submodel.active


def test_car_submodel_from_dict():
    car_submodel = CarSubmodel.from_dict(dict(model_id=1, name='Submodel', active=True))
    assert car_submodel.model_id == 1
    assert car_submodel.name == 'Submodel'
    assert car_submodel.active


def test_car_submodel_to_dict():
    car_submodel = CarSubmodel(model_id=1, name='Submodel', active=True)
    car_submodel2 = car_submodel.to_dict()
    assert car_submodel2['model_id'] == 1
    assert car_submodel2['name'] == 'Submodel'
    assert car_submodel2['active']
