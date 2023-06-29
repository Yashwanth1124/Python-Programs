from array import*
a = array('i',[int(i)for i in input("enter elements:").split()])
a.remove(int(input("enter a index:")))
for x in range(len(a)):
    print(a[x],end=" ")
print()