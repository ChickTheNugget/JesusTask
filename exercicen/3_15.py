from random import randint 
from queue import Queue

days = 5
seconds = 8 * 3600
lanes = 6
shopper_average = 30
lane_change = 60


def chance(a):
    r = randint(1, a)
    return r == 1

served = 0
articles_sold = 0
total_wait_time = 0
total_changes = 0
overtime = 0

class Shopper:
    def __init__(self):
        self.bought_articles = randint(1, 50)
        self.unweighted = chance(20)
        self.bad_card = chance(50)
        self.waiting_time = 0
        self.total_waiting_time = 0
        self.is_served = 0
        self.in_checkout_time = 0
    def checkout_time(self):
        t = 5 * self.bought_articles
        if self.unweighted:
            t += 60
            t -= 5
        if self.bad_card:
            t += 180
        else:
            t += 15
        return t
    def nervous(self):
        if self.waiting_time >= lane_change:
            return True
        else:
            return False
    def tick(self):
        self.total_waiting_time += 1
        self.waiting_time += 1

def min_in_l(l):
    m = 100000
    for i in l:
        m = min(m, len(i))
    for i in range(len(l)):
        if m == len(l[i]):
            return i

for day in range(days):
    l = []
    for i in range(lanes):
        l.append([])
    for second in range(seconds):
        if chance(shopper_average):
            l[min_in_l(l)].append(Shopper())
        for lane in l:
            for i, shopper in enumerate(lane):
                if i == 0 and shopper.is_served:
                    shopper.in_checkout_time += 1
                    if shopper.in_checkout_time >= shopper.checkout_time():
                        del lane[0]
                if i == 0 and not shopper.is_served:
                    shopper.is_served = 1
                    served += 1
                    articles_sold += shopper.bought_articles
                    total_wait_time += shopper.total_waiting_time
                else:
                    if not shopper.is_served and shopper.nervous():
                        if i == 0:
                            if len(l[i + 1]) < len(l[i]):
                                s = lane[i]
                                s.waiting_time = 0
                                del lane[i]
                                l[i + 1].append(s)
                                total_changes += 1
                        elif i == len(lane) - 1:
                            if len(l[i - 1]) < len(l[i]):
                                s = lane[i]
                                s.waiting_time = 0
                                del lane[i]
                                l[i - 1].append(s)
                                total_changes += 1
                        else:
                            if len(l[i + 1]) < len(l[i]) and len(l[i + 1]) < len(l[i - 1]):
                                s = lane[i]
                                s.waiting_time = 0
                                del lane[i]
                                l[i + 1].append(s)
                                total_changes += 1
                            elif len(l[i - 1]) < len(l[i]) and len(l[i - 1]) <= len(l[i + 1]):
                                s = lane[i]
                                s.waiting_time = 0
                                del lane[i]
                                l[i - 1].append(s)
                                total_changes += 1
                shopper.tick()
    while True:
        overtime += 1
        c = 0
        if chance(shopper_average):
            l[min_in_l(l)].append(Shopper())
        for lane in l:
            for i, shopper in enumerate(lane):
                c += 1
                if i == 0 and shopper.is_served:
                    shopper.in_checkout_time += 1
                    if shopper.in_checkout_time >= shopper.checkout_time():
                        del lane[0]
                if i == 0 and not shopper.is_served:
                    shopper.is_served = 1
                    served += 1
                    articles_sold += shopper.bought_articles
                    total_wait_time += shopper.total_waiting_time
                else:
                    if not shopper.is_served and shopper.nervous():
                        if i == 0:
                            if len(l[i + 1]) < len(l[i]):
                                s = lane[i]
                                s.waiting_time = 0
                                del lane[i]
                                l[i + 1].append(s)
                                total_changes += 1
                        elif i == len(lane) - 1:
                            if len(l[i - 1]) < len(l[i]):
                                s = lane[i]
                                s.waiting_time = 0
                                del lane[i]
                                l[i - 1].append(s)
                                total_changes += 1
                        else:
                            if len(l[i + 1]) < len(l[i]) and len(l[i + 1]) < len(l[i - 1]):
                                s = lane[i]
                                s.waiting_time = 0
                                del lane[i]
                                l[i + 1].append(s)
                                total_changes += 1
                            elif len(l[i - 1]) < len(l[i]) and len(l[i - 1]) <= len(l[i + 1]):
                                s = lane[i]
                                s.waiting_time = 0
                                del lane[i]
                                l[i - 1].append(s)
                                total_changes += 1
                shopper.tick()
        if c == 0:
            break
print(served)
print(articles_sold)
print(total_wait_time / 60)
print(total_changes)
print(overtime / 3600)


