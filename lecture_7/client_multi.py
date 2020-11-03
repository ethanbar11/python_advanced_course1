import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8089))


def receiving():
    while True:
        msg = s.recv(1024).decode()
        print(msg)


def sending():
    while True:
        msg = input('Please enter message')
        s.send(msg.encode())


sending_thread = threading.Thread(target=sending)
receiving_thread = threading.Thread(target=receiving)
sending_thread.start()
receiving_thread.start()
