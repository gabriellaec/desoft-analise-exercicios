a=float(input('Depósito Inicial: '))
b=float(input('Taxa de juros (decimal): '))
i=1
atual=a
while i<25:
    print('{0:.2f}'.format(a*(1+b)))
    i+=1
    a*=(1+b) 
print('{0:.2f}'.format(a - atual))
