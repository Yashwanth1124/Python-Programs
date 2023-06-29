a=(1,1,0,1,0,1)
for i in a:
    print(type(i))
b=[]
for i in a:
    b.append(int(i))
c=tuple(b)
print(c)
for i in c:
    print(type(i))
