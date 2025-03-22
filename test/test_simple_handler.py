import socket
from app.handler.simple_http_handler import SimpleHTTPHandler


def test_server_response(server):
    """ Test that the server sends the correct HTTP response. """
    client_socket = socket.create_connection(("localhost", 4221))
    client_socket.sendall(b"GET / HTTP/1.1\r\n\r\n") # Send dummy request
    response = client_socket.recv(1024).decode("utf-8")
    assert response == "HTTP/1.1 200 OK\r\n\r\n"
    client_socket.close()
