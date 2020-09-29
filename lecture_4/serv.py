import socket
import time
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 8089))
serversocket.listen(5)  # become a server socket, maximum 5 connections
print("Started listening!")
while True:
    # Block until new client is connected
    client_socket, address = serversocket.accept()
    buf = client_socket.recv(64)

    if len(buf) > 0:
        print(buf.decode())
