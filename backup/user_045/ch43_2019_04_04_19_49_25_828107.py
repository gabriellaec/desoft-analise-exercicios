s=2
m=0
n=[]
while s<1000:
    n.clear()
    n.append(s)
    i=0
    
    while n[i]>1:
        if n[i]%2==0:
            n.append(n[i]/2)
        else:
            n.append(3*n[i]+1)
        i+=1
    if len(n)>m:
        m=len(n)
        t=n
    s+=1
print(t[0])