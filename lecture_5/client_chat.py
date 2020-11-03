import threading
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8089))
def always_listen():
    while True:
        msg = s.recv(1024).decode()
        print(msg)


def always_sending():
    while True:
        client_msg = input('Your message: ').encode()
        s.send(client_msg)

receiving_thread = threading.Thread(target=always_listen)
receiving_thread.
sending_thread = threading.Thread(target=always_sending)
receiving_thread.start()
sending_thread.start()
