import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("127.0.0.1", 8089))
hello = s.recv(64)
print(hello)
msg = input('Please insert message: ')
s.send(msg.encode())
msg_rcv = s.recv(1048)
print(msg_rcv.decode())
s.close()
