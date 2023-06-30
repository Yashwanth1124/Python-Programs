n = int(input("Enter the no.of elements to read in the list: "))
b = []
c = []
for i in range(n):
    m = int(input())
    b = b+[m]
for i in b:
    c = c+[i*5]
print(b+c)