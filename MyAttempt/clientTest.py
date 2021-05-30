import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host ="192.168.1.110"
port = 5555
s.connect((host,port))

def ts(socket, string):
   socket.send(string.encode())
   data = ''
   data = s.recv(1024).decode() # got it from server

   print(data)

while 2:  # infinite loops
   r = input('enter')
   ts(s, r)

s.close()