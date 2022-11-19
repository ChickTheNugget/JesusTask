from math import *

def dtor(x):
    return x * (pi / 180)

g = 9.8

def posy(x, a, v0, y0):
    return - (g/(2 * (v0 ** 2) * (cos(dtor(a)) ** 2))) * (x ** 2) + tan(dtor(a)) * x + y0

