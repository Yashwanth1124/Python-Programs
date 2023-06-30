a = int(input())
b = []
c = []
for i in range(a):
    m = input("Enter a string: ")
    b+=[m]
for i in b:
    c = c+[(i.lower())]
print(c)