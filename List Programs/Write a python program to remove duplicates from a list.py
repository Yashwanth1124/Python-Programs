n = int(input("Enter no.of elements to read : "))
a = []
for i in range(1,n+1):
    m = int(input())
    a =a+[m]
b = set(a)
print(b)
c=[]
for i in b:
    c=c+[i]
print(c)
    