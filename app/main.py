from app.handler.simple_http_handler import SimpleHTTPHandler
from app.server.http_server import HTTPServer

if __name__ == '__main__':
    simple_http_handler = SimpleHTTPHandler()
    server = HTTPServer("localhost",4221,simple_http_handler)
    server.start()