t=[0]*100
t[0]=1
t[1]=1/2
i=2
while(i<100):
    t[i]=t[i-2]+t[i-1]
    i=i+1
print(t)