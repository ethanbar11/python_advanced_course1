import threading
import socket
import time
import python_advanced_course1.lecture_5.FILE_DAL as DAL
from queue import Queue

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 8089))
serversocket.listen(5)  # become a server socket, maximum 5 connections
print("Started listening!")
# Block until new client is connected
msg_queue = Queue()
client_sockets = []


def receiving_from_certain_client(client_socket):
    is_running = True
    while is_running:
        msg = client_socket.recv(1024)
        if msg != '':
            msg_decoded = msg.decode()
            msg_queue.put(msg_decoded)
        else:
            is_running = False


def sending_from_queue():
    while True:
        msg = msg_queue.get()
        for socket in client_sockets:
            socket.send(msg.encode())


sending_from_queue_thread = threading.Thread(target=sending_from_queue)
sending_from_queue_thread.start()
while True:
    client_socket, address = serversocket.accept()
    client_sockets.append(client_socket)
    client_socket_thread = threading.Thread(target=receiving_from_certain_client,
                                            args=(client_socket,))
    client_socket_thread.start()
