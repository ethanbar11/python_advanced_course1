from python_advanced_course1.lecture_4.zoo import Zoo, Lion
import socket
import pickle

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(("127.0.0.1", 8089))
    lion = Lion('Maor', 25, 25)
    s.send(b'add_lion')
    s.recv(10)
    lion_bytes = pickle.dumps(lion)
    s.send(str(len(lion_bytes)).encode())
    s.recv(10)

    s.send(lion_bytes)
    s.recv(10)
