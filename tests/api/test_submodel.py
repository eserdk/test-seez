async def test_submodels_get(cli):
    resp = await cli.get('/submodels')
    assert resp.status == 200
    resp = await resp.json()
    assert resp
