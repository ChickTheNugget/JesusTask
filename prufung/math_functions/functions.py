from math import log10

print(log10(53))

def fr(n):
    if (n < 10):
        return True
    else:
        d = 10 ** int(log10(n))
        if n % 10 != n // d:
            return False
        else:
            return fr(n % d // 10)



def fi(n):
    while True:
        if (n < 10): 
            return True
        else:
            d = 10 ** int(log10(n))
            if n % 10 != n //d:
                return False
            else:
                n = n % d // 10
    