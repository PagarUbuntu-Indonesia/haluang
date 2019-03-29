import pytest

from app import app as App, CONFIG, PAGE, POST, TEMPLATE


@pytest.fixture(autouse=True)
def app():
    application = App
    application.app_context().push()
    return application


@pytest.fixture
def path_properti(app):
    """
    Variabel direktori website
    """
    return {
        'config': CONFIG,
        'page': PAGE,
        'post': POST,
        'template': TEMPLATE
    }

@pytest.fixture
def client(app):
    client = app.test_client()
    yield client
