

def Lucas_it(n):
    cnt += 1
    l = [2, 1]
    for i in range(n - 2):
        l.append(l[1 + i] + l[i])
    return l[n - 1]

print(Lucas_it(6))

def Lucas_rec(x):
    cnt += 1
    if (x == 1):
        return 2
    if (x == 2):
        return 1
    return Lucas_rec(x - 1) + Lucas_rec(x - 2)

print(Lucas_rec(11))

cache = {1: 2, 2: 1}

def Lucas_rec_cache(x):
    if x in cache:
        return cache[x]
    else:
        cache[x] = Lucas_rec_cache(x - 1) + Lucas_rec_cache(x - 2)
        return cache[x]

    
print(Lucas_rec_cache(11))


