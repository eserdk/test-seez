from bson import json_util
from aiohttp import web

routes = web.RouteTableDef()

from app.core.services.car_make import CarMakeService
from app.core.services.car_model import CarModelService
from app.core.services.car_submodel import CarSubmodelService
from app.core.services.car import CarService


def json_relaxed(*args, **kwargs):
    return json_util.dumps(*args, **kwargs, json_options=json_util.RELAXED_JSON_OPTIONS)


@routes.get('/makes')
async def makes(request):
    return web.json_response([c.to_dict() for c in await CarMakeService().list_all_makes()], dumps=json_relaxed)


@routes.get('/models')
async def models(request):
    return web.json_response([c.to_dict() for c in await CarModelService().list_all_models()], dumps=json_relaxed)


@routes.get('/submodels')
async def submodels(request):
    return web.json_response([c.to_dict() for c in await CarSubmodelService().list_all_submodels()], dumps=json_relaxed)


@routes.get('/cars')
async def cars(request):
    filtr = {}
    errors = {}
    if 'price' in request.query:
        try:
            filtr['price'] = int(request.query['price'])
        except ValueError:
            errors['price'] = 'Only integer value.'
    if 'mileage' in request.query:
        try:
            filtr['mileage'] = int(request.query['mileage'])
        except ValueError:
            errors['mileage'] = 'Only integer value.'

        if errors:
            return web.json_response(errors)

    return web.json_response([c.to_dict() for c in await CarService().list_all_cars_full(filtr)], dumps=json_relaxed)


@routes.post('/cars')
async def car_add(request):
    post = await request.json()
    result = await CarService().create_new_car(**post)
    return web.json_response(result.to_dict(), dumps=json_relaxed)
