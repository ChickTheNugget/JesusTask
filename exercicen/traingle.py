n = int(input())

def pascal(n):
    t = {}
    for i in range(n):
        for j in range(i + 1):
            if i == 0 or j == 0 or j == i:
                t[(i, j)] = 1
            else:
                t[(i, j)] = t[(i - 1, j - 1)] + t[(i - 1, j)]
    return t

tr = {}
def pascal_r(n, k):
    if k > n or n < 0 or k < 0:
        return 0
    if n == 0 or k == 0 or n == k:
        return 1
    return pascal_r(n - 1, k - 1) + pascal_r(n - 1, k)


t1 = pascal(n)

for i in range(n):
    for j in range(i + 1):
        print(t1[(i, j)], end = " ")
    print()

pascal_r(n, 0)
for i in range(n):
    for j in range(i + 1):
        print(tr[(i, j)], end = " ")
    print()