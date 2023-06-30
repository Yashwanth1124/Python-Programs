n = int(input("Enter no.of element to read:"))
b = []
c = []
for i in range(n):
    m = int(input("Elements in b: "))
    b+=[m]
for j in range(n):
    p = int(input("Elements in c: "))
    c+=[p]
a = set(b) & set(c)
print(a)
d =[]
for i in a:
    d = d+[i]
print(d)