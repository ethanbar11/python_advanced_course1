import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8089))
while True:
    s.send(input('Your message: ').encode())
    msg = s.recv(1024).decode()
    print(msg)
