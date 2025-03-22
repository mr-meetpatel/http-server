import socket
from app.handler.base_handler import HTTPHandler

class HTTPServer:
    """
    A simple HTTP server that listens for incoming connections
    and processes them using a provided handler.
    """

    def __init__(self, host: str, port: int, handler: HTTPHandler):
        """
        Initializes the HTTP server with a host, port, and request handler.

        :param host: The hostname or IP address to bind the server.
        :param port: The port number on which the server will listen.
        :param handler: An instance of a class implementing HTTPHandler.
        """
        self.host = host
        self.port = port
        self.handler = handler
        self.server_socket = socket.create_server((host, port), reuse_port=True)

    def start(self) -> None:
        """
        Starts the HTTP server and listens for incoming connections.
        """
        print(f"Starting server on {self.host}:{self.port}")
        with self.server_socket as server_socket:
            while True:
                client_socket, _ = server_socket.accept()
                self.handler.handle(client_socket)
