d=float(input('deposito'))
t=float(input('taxa'))
i=1
while i<25:
    n=d*t**i
    i=i+1
    print('{:.2f}'.format(n))
s=n-d    
print('{:.2f}'.format(s))
    
    
    
    