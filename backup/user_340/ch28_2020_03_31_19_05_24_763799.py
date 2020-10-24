a=[0]*100
s=0
i=0
a[i]=1/2**i
while i<=99:
    i+=1
    s=(a[0]*(1-0.5**i))/0.5
print(s)
    