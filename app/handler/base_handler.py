from abc import ABC, abstractmethod
from socket import socket


class HTTPHandler(ABC):
    """
    Abstraction for handling HTTP requests
    """
    @abstractmethod
    def handle(self, client_socket: socket):
        pass