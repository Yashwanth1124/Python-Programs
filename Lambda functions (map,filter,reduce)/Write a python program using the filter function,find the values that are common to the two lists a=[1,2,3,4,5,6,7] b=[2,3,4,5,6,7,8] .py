a = [1,2,3,4,5,6,7]
b = [2,3,4,5,6,7,8]
common = list(filter(lambda x: x in a,b))
print(common)