n = int(input("Enter no.of elements to read : "))
a = []
b = []
for i in range(1,n+1):
    m =int(input())
    if m%2!=0:
        a =a+[m]
print(a)