a = {int(i)for i in input("Enter values: ").split()}
print(a)
b = []
c = []
for i in a:
    b+=[i]
for i in b:
    i = int(i)
    c = c+[i*2]
print(set(c))