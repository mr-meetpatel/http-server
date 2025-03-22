import threading
import time

import pytest

from app.handler.simple_http_handler import SimpleHTTPHandler
from app.server.http_server import HTTPServer

@pytest.fixture
def simple_handler():
    return SimpleHTTPHandler()

@pytest.fixture
def server(simple_handler):
    """
    starts the http server
    """
    server =  HTTPServer(host="localhost", port=4221,handler=simple_handler)
    thread = threading.Thread(target=server.start,daemon=True)
    thread.start()
    time.sleep(1)
    yield server
    # close server socket after test is finish
    server.server_socket.close()
    time.sleep(1)