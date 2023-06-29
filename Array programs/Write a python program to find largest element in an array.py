from array import*
a = array('i',[int(i)for i in input("enter elements:").split()])
#print("max = ",max(a))
max=a[0]
for i in range(len(a)):
    if a[i]>max:
        max = a[i]
print(max)