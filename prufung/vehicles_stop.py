from random import randrange

class Car:
    def __init__(self, v = 0):
        self.x = 0
        if v != 0:
            self.v_x = v
        else:
            self.v_x = randrange(10, 30)
        self.a_x = 0

    def move(self):
        self.x += self.v_x
    
    def accelerate(self, a):
        self.a_x = a
        self.v_x += self.a_x

    def danger(self, second_car_pos):
        if second_car_pos - self.x < 100:
            return True
        else:
            return False

    def __str__(self):
        res = f"pos {self.x} speed {self.v_x} acceleration {self.a_x}"
        return res



c = Car()
second_car_pos = 1000

while True:
    if (c.danger(second_car_pos)):
        c.accelerate(-5)
    if (c.v_x < 0):
        break
    c.move()

print(c.x)
    