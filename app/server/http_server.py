import socket

class HTTPServer:
    def __init__(self, host: str, port: int):
        """
        Initializes the HTTP server with a specified host & port

        :param host: The hostname or IP address to bind the server.
        :param port: The port number on which the server will listen.
        """
        self.host = host
        self.port = port
        self.server_socket = socket.create_server((host,port),reuse_port=True)

    def start(self) -> None:
        """
        Starts the HTTP server and listens for incoming connections.
        """
        print(f"Starting server on {self.host}:{self.port}")

        with socket.create_server((self.host, self.port), reuse_port=True) as server_socket:
            while True:
                # Accept client connection
                client_socket, _ = server_socket.accept()


if __name__ == '__main__':
    server = HTTPServer("localhost",4221)
    server.start()