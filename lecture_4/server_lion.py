import socket
import time
import pickle
import os
from python_advanced_course1.lecture_4.zoo import Zoo

ZOO_FILE_PATH = 'zoo.bin'
if os.path.exists(ZOO_FILE_PATH):
    with open(ZOO_FILE_PATH, 'rb') as zoo_file:
        zoo = pickle.loads(zoo_file.read())
else:
    zoo = Zoo()
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 8089))
serversocket.listen(5)  # become a server socket, maximum 5 connections
print("Started listening!")
# while True:
# Block until new client is connected
client_socket, address = serversocket.accept()
cmd = client_socket.recv(100).decode()
client_socket.send(b'Ack')
if cmd == 'add_lion':
    lion_size = int(client_socket.recv(20).decode())
    client_socket.send(b'Ack')
    lion_bytes = client_socket.recv(lion_size)
    client_socket.send(b'Ack')
    lion = pickle.loads(lion_bytes)
    print(lion.name)
    zoo.add_lion(lion)
elif cmd == 'remove_lion':
    lion_bytes = client_socket.recv(1024)
    lion = pickle.loads(lion_bytes)
    zoo.remove_lion(lion.name)
elif cmd == 'get_lions_amount':
    client_socket.send(str(zoo.get_lions_amonut()).encode())

serversocket.close()
with open(ZOO_FILE_PATH, 'wb') as zoo_file:
    pickle.dump(zoo, zoo_file)
