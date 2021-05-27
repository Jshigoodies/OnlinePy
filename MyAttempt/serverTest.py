# Honestly, I'm still too stupid to figure this out.

import socket
from _thread import *
import sys

server = "192.168.1.110"
port = 5555

s = socket.socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(server, port)  # connect to localhost and at that port

s.listen(2) # look for 2 connections

def threaded_client(conn):
    conn.send(str.encode("Connecting"))

    reply = ""
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending : ", reply)
        except:
            break
    print("Lost connection")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,)) # multi tasking. Or known as multi threading. Multiple processes go in the background.