x = [int(i)for i in input("enter values:").split()]
l = int(input("enter required length: "))
for i in x:
    if i>l:
        print(i,end=" ")