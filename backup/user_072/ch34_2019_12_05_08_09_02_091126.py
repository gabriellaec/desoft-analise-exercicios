a=float(input('Depósito Inicial: '))
b=float(input('Taxa de juros (decimal): '))
i=1
primeira_VI=a
while i<25:
    y=a*(1+b)
    print('{0:.2f}'.format(y))
    i+=1
    a=y    
print('{0:.2f}'.format(a-primeira_VI))
