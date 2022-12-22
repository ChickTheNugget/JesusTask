from queue import Queue
from random import randint

days = 10
seconds = 6 * 3600
people = 50
average_time = 45
beer_time = 30


class Customer:
    def __init__(self):
        self.taux = 0
        self.wait = 0
        self.dead = 0
    def waiting(self):
        return self.wait > 0
    def coma(self):
        return self.taux >= 3
    def order_beer(self): 
        self.taux += randint(200, 300) / 1000
    def tick(self):
        self.taux *= (35999 / 36000)

def arrival(a):
    r = randint(1, a)
    return r == 1

beers = 0
coma_num = 0
rest = 0

for day in range(days):
    l = []
    q = Queue()
    bar = 30
    for i in range(people):
        l.append(Customer())
    for second in range(seconds):
        if arrival(average_time):
            for i in range(500):
                r = randint(0, people - 1)
                if l[r].waiting():
                    continue
                l[r].wait = 1
                q.put(l[r])
                break
        if bar > 0 and not q.empty():
            bar -= 1
        elif bar <= 0:
            person = q.get()
            person.wait = 0
            person.order_beer()
            beers += 1
            bar = beer_time

        for person in l:
            if person.coma() and person.dead == 0:
                coma_num += 1
                person.dead = 1
            else:
                person.tick()
    rest += q.qsize()

print(beers)
print(coma_num)
print(rest)