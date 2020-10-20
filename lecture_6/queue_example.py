import queue

q = queue.Queue()

q.put('2')
q.put('1')
print(q.get())
print(q.get())
