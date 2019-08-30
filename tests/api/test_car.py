import json


async def test_cars_get(cli):
    resp = await cli.get('/cars')
    assert resp.status == 200
    resp = await resp.json()
    assert resp


async def test_cars_post(cli):
    data = {
        'year': 1997, 'mileage': 20000, 'price': 100500, 'body_type': 'Hatchback',
        'transmission': 'Automatic', 'fuel_type': 'Diesel', 'exterior_color': 'White',
    }
    resp = await cli.post('/cars', data=json.dumps(data))
    assert resp.status == 200
    resp = await resp.json()
    assert '_id' in resp
    assert '$oid' in resp['_id']
