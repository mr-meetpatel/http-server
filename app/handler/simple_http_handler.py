import socket
from app.handler.base_handler import HTTPHandler

class SimpleHTTPHandler(HTTPHandler):
    """
    Handles HTTP requests by sending a fixed 200 OK response.
    """

    def handle(self, client_socket: socket.socket) -> None:
        response = "HTTP/1.1 200 OK\r\n\r\n"
        client_socket.sendall(response.encode("utf-8"))
        client_socket.close()
