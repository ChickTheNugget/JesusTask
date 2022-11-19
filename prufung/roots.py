from math import *

def func_1(x):
    return cos(x) ** 3 + 0.5

def func_2(x):
    return x + 1

def root_it(f, beg, end, prec):
    while True:
        mid = (beg + end) / 2
        v = f(mid)
        vbeg = f(beg)
        if v == 0:
            return mid
        if v * vbeg > 0:
            beg = mid
        else:
            end = mid
        
        if (abs(beg - end) <= prec):
            return (beg + end) / 2

def root_rec(f, beg, end, prec):
    mid = (beg + end) / 2
    v = f(mid)
    vbeg = f(beg)
    if (abs(beg - end) <= prec):
            return (beg + end) / 2
    if v == 0:
        return mid
    if v * vbeg > 0:
        return root_rec(f, mid, end, prec)
    else:
        return root_rec(f, beg, mid, prec)
    


print(root_it(func_1, 0, 3.141592, 0.01))
print(root_rec(func_1, 0, 3.141592, 0.01))