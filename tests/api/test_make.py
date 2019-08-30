async def test_makes_get(cli):
    resp = await cli.get('/makes')
    assert resp.status == 200
    resp = await resp.json()
    assert resp
