import threading
import time

import pytest

from app.server.http_server import HTTPServer


@pytest.fixture
def server():
    """
    starts the http server
    """
    server =  HTTPServer(host="localhost",port=4221)
    thread = threading.Thread(target=server.start,daemon=True)
    thread.start()
    time.sleep(1)
    yield server
    # close server socket after test is finish
    print("stop server")
    server.server_socket.close()
