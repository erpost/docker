import socket

print('The IP Address of this Docker is:', socket.gethostbyname(socket.gethostname()))
