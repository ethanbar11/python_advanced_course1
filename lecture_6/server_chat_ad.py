import threading
import socket
import time
import python_advanced_course1.lecture_5.FILE_DAL as DAL

DB_PATH = r"C:\Users\Borat\int_database.txt"
conn = DAL.get_connection(DB_PATH)
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('127.0.0.1', 8089))
serversocket.listen(5)  # become a server socket, maximum 5 connections
print("Started listening!")
# Block until new client is connected
client_socket, address = serversocket.accept()
# Creating new thread here that talks with the client specifically.
is_active = True


def always_listen():
    while True:
        msg = client_socket.recv(1024).decode()
        print(msg)


def always_sending():
    while True:
        client_msg = input('Your message: ').encode()
        client_socket.send(client_msg)


receiving_thread = threading.Thread(target=always_listen)
sending_thread = threading.Thread(target=always_sending)
receiving_thread.start()
sending_thread.start()

# while is_active:
#     msg = client_socket.recv(1024).decode()
#     if msg != '':
#         print(msg)
#         # DAL.insert_message(conn, "Client", msg)
#         client_msg = input('Your message: ').encode()
#         client_socket.send(client_msg)
# DAL.insert_message(conn, "Server", client_msg)

# else:
#     is_active = False
