l = [0] * 6
c = 0
sm = 0

file = open("fonseca.txt", 'r')
for i in file:
    a, b, c = i.split()
    a = int(a)
    b = int(b)
    c = int(c)
    l[a] -= c
    l[b] += c
    c += 1
    sm += abs(c)

for i in range(5):
    print(f"Bank {i + 1} : {l[i + 1]}")
    
print(sm / c)
    