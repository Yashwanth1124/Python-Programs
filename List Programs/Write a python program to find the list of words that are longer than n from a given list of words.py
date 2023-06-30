a = int(input("Enter no.of elements to read: "))
b = []
for i in range(a):
    m = input("Enter a string\n")
    b+=[m]
c = len(b)
for i in b:
    if len(i)>c:
        print(i)