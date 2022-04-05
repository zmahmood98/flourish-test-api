import json

class TestCases:
    def test_home_route(client):
        res = client.get('/')
        assert res.status == '200 OK'

