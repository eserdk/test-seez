from app.core.domain.car import Car


def test_car_init():
    car = Car(submodel_id=100, year=1999, mileage=20000, price=300000, body_type='Sedan',
              transmission='Automatic', fuel_type='Petrol', exterior_color='White')
    assert car.submodel_id == 100
    assert car.year == 1999
    assert car.mileage == 20000
    assert car.price == 300000
    assert car.body_type == 'Sedan'
    assert car.transmission == 'Automatic'
    assert car.fuel_type == 'Petrol'
    assert car.exterior_color == 'White'


def test_car_from_dict():
    car = Car.from_dict(
        dict(submodel_id=111, year=2009, mileage=55000, price=1000000, body_type='SUV',
             transmission='Manual', fuel_type='Diesel', exterior_color='Black'))
    assert car.submodel_id == 111
    assert car.year == 2009
    assert car.mileage == 55000
    assert car.price == 1000000
    assert car.body_type == 'SUV'
    assert car.transmission == 'Manual'
    assert car.fuel_type == 'Diesel'
    assert car.exterior_color == 'Black'


def test_car_to_dict():
    car = Car(submodel_id=111, year=2009, mileage=55000, price=1000000, body_type='SUV',
              transmission='Manual', fuel_type='Diesel', exterior_color='Black')
    car2 = car.to_dict()
    assert car2['submodel_id'] == 111
    assert car2['year'] == 2009
    assert car2['mileage'] == 55000
    assert car2['price'] == 1000000
    assert car2['body_type'] == 'SUV'
    assert car2['transmission'] == 'Manual'
    assert car2['fuel_type'] == 'Diesel'
    assert car2['exterior_color'] == 'Black'
