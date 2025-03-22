import socket
from multiprocessing.connection import Connection

import pytest


def test_client_connection(server):
    """
    Test that a client can successfully
    connect to the server.
    """
    try:
        client_socket = socket.create_connection(("localhost",4221))
        assert client_socket is not None
        host,port = client_socket.getpeername()
        assert host == "127.0.0.1"
        assert port == 4221
    except Exception as e:
        pytest.fail(f"client failed to connect to the server: {e}")

def test_multiple_client_connections(server):
    """
    Test that a multiple client can successfully
    connect to the server.
    """
    for _ in range(3):
        try:
            client_socket = socket.create_connection(("localhost",4221))
            assert client_socket is not None
            host,port = client_socket.getpeername()
            assert host == "127.0.0.1"
            assert port == 4221
        except Exception as e:
            pytest.fail(f"client failed to connect to the server: {e}")

def test_client_cannot_connection_when_server_is_down():
    """
    Test that a client cannot connect when server is down.
    """
    with pytest.raises(ConnectionRefusedError) as cre:
        socket.create_connection(("localhost",4221))
    assert cre.type == ConnectionRefusedError
    assert cre.value.errno == 111
    assert cre.value.strerror == "Connection refused"


