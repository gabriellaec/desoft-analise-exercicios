d=float(input('deposito'))
t=float(input('taxa'))
n=0
s=0
i=1
while i<25:
    n=d*t**i
    s=s+n
    print(n) 
    i=i+1
print(s)
    
    
    
    