from array import*
a = array('i',[int(i)for i in input("enter elements:").split()])
duplicate=[]
for i in a:
    if a.count(i)>1:
        duplicate.append(i)
print(duplicate)