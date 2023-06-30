def fun(n):
    return lambda x:x*n
a = int(input("Enter the argument:"))
b = int(input("Enter the number:"))
result = fun(a)
print(result(b))