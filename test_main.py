import json
import unittest

class TestCases(unittest.TestCase):
    def test_home_route(self, client):
        res = client.get('/')
        assert res.status == '200 OK'


if __name__ == "__main__":
    unittest.main()
