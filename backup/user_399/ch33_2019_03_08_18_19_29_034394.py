P=[0]*100
i=0
while i<100:
    P[i]=1/(2**i)
    i+=1
print(sum(P))