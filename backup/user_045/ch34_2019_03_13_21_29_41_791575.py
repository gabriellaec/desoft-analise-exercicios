d=float(input('deposito'))
t=float(input('taxa'))
s=0
i=1
while i<25:
    n=d*t**i
    s=s+n
    i=i+1
    print('{:.2f}'.format(n))
print('{:.2f}'.format(s))
    
    
    
    