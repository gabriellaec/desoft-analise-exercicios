v=[-2,3,4,-5,6,7,8,-9,]
i=0
while i<len(v):
    if v[i]<0:
        v[i]=0
    i+=1
print(v)