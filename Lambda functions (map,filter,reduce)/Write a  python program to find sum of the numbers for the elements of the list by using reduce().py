from functools import reduce
a = [int(i)for i in input("Enter values:").split()]
sum = reduce(lambda x,y: x+y,a)
print(sum)