a = [int(i)for i in input("enter numbers:").split()]
power = list(map(lambda x:2**x ,a))
print(power)