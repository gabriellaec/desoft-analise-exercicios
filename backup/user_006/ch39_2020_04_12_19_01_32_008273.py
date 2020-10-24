n=2
maxi=0
while n<1000:
    s=n
    i=1
    while s>1:
        if s%2==0:
            s=s/2
            i=i+1
        else:
            s=3*s+1
            i=i+1
    if i>maxi:
        maxi=n
    n=n+1
    
print(maxi)