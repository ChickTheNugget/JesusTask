from math import sqrt

def suite_heron_i(A, n):
    u = [0] * (n + 1)
    u[0] = 1
    for i in range(1, n + 1):
        u[i] = (u[i - 1] + A / u[i - 1]) / 2
    return u[n]

def suite_heron_r(A, n):
    if (n == 0):
        return 1
    else:
        return (suite_heron_r(A, n - 1) + A / suite_heron_r(A, n - 1)) / 2

print(suite_heron_i(36, 5))
print(suite_heron_r(36, 5))

# elle tend vers la racine de A

def suite_heron_n(A):
    u = [1]
    n = 0
    while True:
        if abs(u[n] - sqrt(A)) < 1e-6:
            if (n == 0): 
                l = 1
            else:
                l = [u[n], u[n - 1], n] 
            return l
        u.append((u[n] + A / u[n]) / 2)
        n += 1

print(suite_heron_n(10287382911))
