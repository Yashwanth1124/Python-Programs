#a =list(map(int,input().split()))
a = [int(i)for i in input("enter numbers:").split()]
b = list(filter(lambda x: (x%2 == 0),a))
print(b)