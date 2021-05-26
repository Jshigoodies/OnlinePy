import socket
from _thread import *
import sys

server = "192.168.1.110"  # this is my localhost. So it doesn't matter if this shows
port = 5555
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Ipv4 address

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)  # listens for connections. 2 = only 2 clients can connect

print("Server Started\nWaiting for connection")


def threaded_client(connection):

    reply = ""
    while True:
        try:
            data = connection.recv(2048)
            reply = data.decode("utf-8")  # when the server receives information, it is encoded. So we have to decode it to read it. utf-8 is a format
            if not data:  # server gets a connection, but client has no information: break
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            connection.sendall(str.encode(reply))
        except Exception:
            break


while True:  # continuously find connections until 2 are found
    connection, address = s.accept()  # accept any connection. Stores connection and address
    print("Connected to: ", address)

    start_new_thread(threaded_client(), (connection,))


# This is actually pretty cool.
# I basically multi threading.
# Thread is basically another
# process that is going
# in the background. In this case the def method called
# threaded_client is going to happen simultaneously without waiting for the other initial method to finish
