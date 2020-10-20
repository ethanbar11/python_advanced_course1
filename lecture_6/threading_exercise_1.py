import threading
import time
class StrawManager:
    def __init__(self):
        self.straw_amount = 0
        self.lock = threading.Lock()

    def add_straw(self):
        self.lock.acquire()
        self.straw_amount += 1
        self.lock.release()

    def remove_straw(self):
        self.lock.acquire()
        self.straw_amount -= 1
        self.lock.release()

    def print_straw_amount(self):
        print(self.straw_amount)


if __name__ == '__main__':
    straw_manager = StrawManager()
    for i in range(10):
        t = threading.Thread(target=straw_manager.add_straw)
        t.start()
    time.sleep(0.01)
    straw_manager.print_straw_amount()
