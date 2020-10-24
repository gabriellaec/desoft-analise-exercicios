m=0
n=[]
n.append(2)
while n[0]<1000:
    i=0
    n[0]+=1
    while n[i]>1:
        if n[i]%2==0:
            n.append(n[i]/2)
        else:
            n.append(3*n[i]+1)
        i+=1
    if len(n)>m:
        m=len(n)
        t=n
print(t[0])
        
     
    