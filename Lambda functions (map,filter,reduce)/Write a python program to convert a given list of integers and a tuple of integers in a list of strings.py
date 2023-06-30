a = [1,2,3,4,5]
b = (1,2,3,4,5)
convert_list = list(map(lambda x:str(x),a))
convert_tuple = tuple(map(lambda x:str(x),b))
print(convert_list)
print(convert_tuple)