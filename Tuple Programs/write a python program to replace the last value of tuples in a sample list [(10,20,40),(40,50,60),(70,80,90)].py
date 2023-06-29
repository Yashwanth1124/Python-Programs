a=[(10,20,30),(40,50,60),(70,80,90)]
d=[]
for i in a:
    h=list(i)
    h[2]="100"
    c=tuple(h)
    d+=[c]
print(d)
#h=list(b)
#h[2]="100"
#b=tuple(h)
#print(b)