#method_1
from array import*
a = array('i',[int(i)for i in input("enter elements:").split()])
b = sum(a)
print("sum of the array elements:",b)

#method-2
from array import*
a = array('i',[int(i)for i in input('enter elements:').split()])
sum = 0
for i in a:
    sum+=i
print(sum)