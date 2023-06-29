a = [(10,20),(23,45,67),(34,67,89,9,89),(345),(1,2,3,4)]
s = sorted(a, key = lambda x : sum([len(str(i)) for i in x]))
print(s)