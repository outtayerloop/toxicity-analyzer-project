import pytest
from tests.ServerThread import start_server, stop_server


@pytest.fixture(autouse=True, scope='session')
def manage_server():
    """
    Start the server before integration tests are ran
    and shut it down afterwards.
    """
    start_server()
    yield
    stop_server()