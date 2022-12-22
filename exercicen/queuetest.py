from queue import Queue

q = Queue()
q.put(1)
q.put(2)
q.put(3)
#1, 2, 3
print(q.queue[0])
print(q.get())
#zero is the first guy out