d=float(input('deposito'))
dm=float(input('deposito mensal'))
t=float(input('taxa'))
i=1
t+=1
v=d
while i<25:
    d=d+dm
    d=d*t
    i=i+1
    print('{:.2f}'.format(n))

s=n-v-dm*24 
print('{:.2f}'.format(s))