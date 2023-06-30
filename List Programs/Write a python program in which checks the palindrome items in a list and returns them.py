a = int(input())
b = []
for i in range(a):
    m = input("Enter a string: ")
    if m[::-1]==m:
        b+=m
print(b)