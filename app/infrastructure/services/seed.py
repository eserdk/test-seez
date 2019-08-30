import math
import os

from dateutil import parser


def parse(date):
    if isinstance(date, float):
        return None
    elif isinstance(date, str):
        return parser.parse(date)


def handle_active(active):
    return True if active == 't' else False


def handle_int(integer):
    if isinstance(integer, int):
        return integer
    elif isinstance(integer, str):
        return int(integer)
    elif isinstance(integer, float):
        return int(integer) if not math.isnan(integer) else None


async def seed_db():
    from app.infrastructure.db import db
    data = _load_data()
    for i, r in data.iterrows():
        make_created = False
        model_created = False
        submodel_created = False
        make = await db.car_makes.find_one({'id_old': r['make_id']})
        if make is None:
            make_created = True
            make = await db.car_makes.insert_one({
                'id_old': r['make_id'],
                'name': r['make_name'],
                'active': handle_active(r['make_active']),
                'created_at': parse(r['make_created_at']),
                'updated_at': parse(r['make_updated_at'])
            })
        model = await db.car_models.find_one({'id_old': r['model_id']})
        if model is None:
            model_created = True
            model = await db.car_models.insert_one({
                'id_old': r['model_id'],
                'name': r['model_name'],
                'make_id': make['_id'] if not make_created else make.inserted_id,
                'active': handle_active(r['model_active']),
                'created_at': parse(r['model_created_at']),
                'updated_at': parse(r['model_updated_at']),
            })
        submodel = await db.car_submodels.find_one({'id_old': r['submodel_id']})
        if submodel is None:
            submodel_created = True
            submodel = await db.car_submodels.insert_one({
                'id_old': r['submodel_id'],
                'name': r['submodel_name'],
                'active': handle_active(r['submodel_active']),
                'created_at': parse(r['submodel_created_at']),
                'updated_at': parse(r['submodel_updated_at']),
                'model_id': model['_id'] if not model_created else model.inserted_id,
            })
        car = await db.cars.find_one({'id_old': r['car_id']})
        if car is None:
            car = await db.cars.insert_one({
                'id_old': r['car_id'],
                'year': handle_int(r['car_year']),
                'mileage': handle_int(r['car_mileage']),
                'price': handle_int(r['car_price']),
                'body_type': r['car_body_type'],
                'transmission': r['car_transmission'],
                'fuel_type': r['car_fuel_type'],
                'exterior_color': r['car_exterior_color'],
                'image_uris': parse(r['car_image_uris']),
                'created_at': parse(r['car_created_at']),
                'updated_at': parse(r['car_updated_at']),
                'submodel_id': submodel['_id'] if not submodel_created else submodel.inserted_id,
            })
    await db.cars.update_many({}, {'$unset': {'id_old': ''}})
    await db.car_submodels.update_many({}, {'$unset': {'id_old': ''}})
    await db.car_models.update_many({}, {'$unset': {'id_old': ''}})
    await db.car_makes.update_many({}, {'$unset': {'id_old': ''}})


def _load_data():
    import pandas as pd
    from config import ROOT_DIR
    data_dir = os.path.join(ROOT_DIR, 'data', 'seed')

    makes = pd.read_csv(os.path.join(data_dir, 'makes.csv'))
    models = pd.read_csv(os.path.join(data_dir, 'models.csv'))
    submodels = pd.read_csv(os.path.join(data_dir, 'submodels.csv'))
    cars = pd.read_csv(os.path.join(data_dir, 'cars.csv'))

    cars.drop(labels=['make_id', 'model_id'], inplace=True, axis=1)
    makes.rename(columns={x: f'make_{x}' for x in makes.columns}, inplace=True)
    models.rename(columns={x: f'model_{x}' for x in models.columns}, inplace=True)
    submodels.rename(columns={x: f'submodel_{x}' for x in submodels.columns}, inplace=True)
    cars.rename(columns={x: f'car_{x}' for x in cars.columns}, inplace=True)

    data = makes.merge(models, left_on='make_id', right_on='model_make_id')
    data = data.merge(submodels, left_on='model_id', right_on='submodel_model_id')
    data = data.merge(cars, left_on='submodel_id', right_on='car_submodel_id')
    data.drop(labels=['model_make_id', 'submodel_model_id'], inplace=True, axis=1)
    return data


def _perform_data_mutations_and_save():
    data = _load_data()
    data.to_csv('data.csv', index=False)
    return data
