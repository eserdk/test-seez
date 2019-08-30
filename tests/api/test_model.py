async def test_models_get(cli):
    resp = await cli.get('/models')
    assert resp.status == 200
    resp = await resp.json()
    assert resp
