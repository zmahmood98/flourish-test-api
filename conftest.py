import pytest
from flourish_app import create_app


@pytest.fixture
def app(self):
    app = create_app(config_file='.flourish_app.settings.py')
    return app

@pytest.fixture
def client(app):
    return app.test_client()
