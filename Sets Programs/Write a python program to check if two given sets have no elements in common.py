a = {int(i)for i in input("Enter values: ").split()}
print(a)
b = {int(j)for j in input("Enter values: ").split()}
print(b)
c = a & b
print(len(c))
if len(c)==0:
    print("There is nO common element")
else:
    print("There is common element")