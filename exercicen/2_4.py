def pascal_r(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return pascal_r(n - 1, k - 1) + pascal_r(n - 1, k)

cache = {}
def pascal_rc(n, k):
    global cache
    if n < 0 or k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    if (n, k) in cache:
        return cache[(n, k)]
    x = pascal_rc(n - 1, k - 1) + pascal_rc(n - 1, k)
    cache[(n, k)] = x
    return x

def pascal_i(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    t = {}
    for i in range(n):
        for j in range(i + 1):  # on calcule uniquement l5es nombres dont on aura besoin dans la suite        
            if j == 0 or j == i:
                t[(i, j)] = 1
            else:
                t[(i, j)] = t[(i - 1, j - 1)] + t[(i - 1, j)]
#        t[(i, 0)] = 1  # version plus simple que les 5 lignes précédentes, mais plus lente
#        t[(i, i)] = 1
#        for j in range(1, i):
#            t[(i, j)] = t[(i - 1, j - 1)] + t[(i - 1, j)]  # on construit tout le triangle supérieur
    return t[(n - 1, k - 1)] + t[(n - 1, k)]

def fact(n):
    return 1 if n<=1 else n * fact(n - 1)

def pascal_f(n, k):
    if n < 0 or k < 0 or k > n:
        return 0
    return fact(n) // (fact(k) * fact(n - k))


ftest = pascal_i  # utilisation facultative d'un pointeur de fonction, pour tester les différentes fonctions

li = int(input("Entrez N (le nombre de lignes à afficher) : "))
for i in range(li):
    for j in range(i + 1):
        print(ftest(i, j), end = " ")
    print()
for i in range(li, li + 10):
    s = 0
    for j in range(i + 1):
        s += ftest(i, j)
    print(s)
    
a = int(input("\nEntrez a : "))
li = int(input("Entrez M (le nombre de lignes à afficher) : "))
file = open("pascal.txt", "w")
for i in range(li):
    s = ""
    for j in range(i + 1):
        s += " " if ftest(i, j) % a == 0 else "*"
    file.write(s + "\n")
file.close()