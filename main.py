import DelverHttp

server = DelverHttp.DelverHttpServer()
server.serve_forever()
server.server_close()