from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse
import threading

HOST = "192.168.0.137"
PORT = 8000

class StringHolder():
    def __init__(self):
        self.contents=None

class EventHttpServer(HTTPServer):
    def makeHandlerClassForListener(self, event, holder):
        class CustomHandler(SimpleHTTPRequestHandler, object):

            def _set_response(self):
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()

            def __init__(self, *args, **kwargs):
                self.event = event
                self.holder=holder
                super(CustomHandler, self).__init__(*args, **kwargs)

            def do_GET(self):
                self._set_response()
                query = urlparse(self.path).query
                self.holder.contents=query
                self.event.set()
        return CustomHandler
    
    def __init__(self):
        self.event=threading.Event()
        self.stringHolder=StringHolder()
        self.handlerClass=self.makeHandlerClassForListener(self.event,self.stringHolder)
        
        super().__init__((HOST,PORT), self.handlerClass)
        self.t1=None

