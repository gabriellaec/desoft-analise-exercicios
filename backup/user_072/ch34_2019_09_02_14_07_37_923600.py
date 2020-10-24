a=float(input('Depósito Inicial: '))
b=float(input('Taxa de juros (%): '))
i=0
while i<25:
    y=a*(1+b)
    print(y)
    i+=1
    a=y    
    
