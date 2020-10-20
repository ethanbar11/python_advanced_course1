import threading
import time

def work():
    for i in range(100):
        print(i)


if __name__ == '__main__':
    for i in range(5):
        t = threading.Thread(target=work)
        t.start()
        time.sleep(1)
