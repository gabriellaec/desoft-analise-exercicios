d=float(input('deposito'))
dm=float(input('deposito mensal'))
t=float(input('taxa'))
i=1
t+=1
while i<25:
    n=d*t
    d=n+dm
    i=i+1
    print('{:.2f}'.format(n))

s=d-n-dm*24    
print('{:.2f}'.format(s))