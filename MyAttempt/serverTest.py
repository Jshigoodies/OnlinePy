import socket
from threading import *

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "192.168.1.110"
port = 5555
print(host)
print(port)
serversocket.bind((host, port))

class client(Thread):
    def __init__(self, socket, address):
        Thread.__init__(self)
        self.sock = socket
        self.addr = address
        self.start()

    def run(self):
        while 1:
            print('Client sent:', self.sock.recv(1024).decode())
            self.sock.send('Oi you sent something to me'.encode())


# runner
serversocket.listen(5)
print ('server started and listening')
while 1:  # infinite loops
    clientsocket, address = serversocket.accept() # literally the same thing
    client(clientsocket, address)