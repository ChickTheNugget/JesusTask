from queue import Queue
from random import randint
#toute les 40 sec, patience 2 - 10 min, servir 30sec - 5min, 10 jours, 8 heures

average_client = 40
days = 10
seconds = 8 * 3600
time_to_serve = [30, 300]
patience = [120, 600]

class Guichet:
    def __init__(self):
        self.time_used = 0
    def is_busy(self):
        return self.time_used > 0
    def tick(self):
        if self.is_busy():
            self.time_used -= 1
    def new_customer(self):
        self.time_used = randint(time_to_serve[0], time_to_serve[1])
    def __str__(self):
        return f"guichet, occupé pendant {self.time_busy} secondes"

def arrival(a):
    r = randint(1, a)
    return r == 1

served = 0
impatient = 0
unlucky = 0
wait_time = 0

for day in range(days):
    g = Guichet()
    q = Queue()
    qs = Queue()
    for second in range(seconds):
        if arrival(average_client) == 1:
            client_patience = second + randint(patience[0], patience[1])
            q.put(client_patience)
            qs.put(second)
        if not g.is_busy():
            while not q.empty() and q.queue[0] < second:
                q.get()
                qs.get()
                impatient += 1
            if not q.empty():
                g.new_customer()
                served += 1
                q.get()
                wait_time += second - qs.get()
        g.tick()
    while not q.empty():
        customer = q.get()
        qs.get()
        if customer < seconds:
            impatient += 1
        else:
            unlucky += 1

print(served)
print(impatient)
print(unlucky)
print(wait_time / served)

qt = Queue()
qt.put(1)
qt.put(2)
