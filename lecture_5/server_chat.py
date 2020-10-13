import socket
import time

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 8089))
serversocket.listen(5)  # become a server socket, maximum 5 connections
print("Started listening!")
# Block until new client is connected
client_socket, address = serversocket.accept()
is_active = True
while is_active:
    msg = client_socket.recv(1024).decode()
    if msg != '':
        print(msg)
        client_socket.send(input('Your message: ').encode())
    else:
        is_active = False
