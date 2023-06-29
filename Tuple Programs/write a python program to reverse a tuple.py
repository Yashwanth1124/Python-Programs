a=int(input("Enter the no.of elements to read\n"))
b=()
for i in range(a):
    c=input()
    b=b+tuple(c)
print(b)
print(b[::-1])
