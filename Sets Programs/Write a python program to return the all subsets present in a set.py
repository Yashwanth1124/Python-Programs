a = {int(i)for i in input("Enter values: ").split()}
print(a)
c = len(a)
n = 2**c
for i in range(n):
    s = set()
    for j in range(n):
        if i & (i<<j):
            s.add(list(a)[j])
    print(s)