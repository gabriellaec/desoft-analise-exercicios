d=float(input('deposito'))
dm=float(input('deposito mensal'))
t=float(input('taxa'))
i=1
t+=1
v=d
while i<25:
    n=d*t
    d=n+dm
    i=i+1
    print('{:.2f}'.format(n))

s=n-v-dm*23 
print('{:.2f}'.format(s))