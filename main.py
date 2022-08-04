import EventHttp
import threading

def parse(queryString): # Move to Delver module
    if len(queryString.split("&")) < 1:
        return
    query_components = dict(qc.split("=") for qc in queryString.split("&"))
    print(query_components['scryfallid'])

def mainFunction():
    print("Main Starting")
    while True:
        server.event.wait()
        parse(server.stringHolder.contents)
        server.event.clear()

server = EventHttp.EventHttpServer()
t1=threading.Thread(target=mainFunction)
server.t1=t1
t1.start()

server.serve_forever()
server.server_close()



