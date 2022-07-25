from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse

HOST = "192.168.0.137"
PORT = 8000

class DelverHttp(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response_only(200)
        query = urlparse(self.path).query
        query_components = dict(qc.split("=") for qc in query.split("&"))
        print(query_components['scryfallid'])


class DelverHttpServer(HTTPServer):
    def __init__(self):
        super().__init__((HOST,PORT), DelverHttp)