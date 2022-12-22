from queue import Queue
from random import randint
#put, get, empty, qsize, full
#toute les 240 sec, 300 sec un lavage, 10 * 3600 sec jour, 10 jours

class CarWash:
    def __init__(self , tw):
        self.time_wash = tw
        self.time_remaining = 0
    def busy(self):
        return self.time_remaining > 0
    def tick(self):
        if self.busy ():
            self.time_remaining -= 1
    def start_wash (self):
        self.time_remaining = self.time_wash
    def __str__(self):
        s = f"lavage , total = {self.time_wash},"
        return s + f" reste = {self.time_remaining}"

need = 300
arrival_time = 240
days = 10
seconds = 10 * 3600
total_wait = 0
total_cars = 0
angry = 0

def arrival(a):
    r = randint(1, a)
    return r == 1

for day in range(days):
    car_wash = CarWash(need)
    q = Queue()
    for second in range(seconds):
        if arrival(arrival_time):
            q.put(second)
        if not q.empty() and not car_wash.busy():
            car_wash.start_wash()
            total_wait += second - q.get()
            total_cars += 1
        car_wash.tick()
    angry += q.qsize()

print(total_cars)
print(angry)
print(total_wait / total_cars)

