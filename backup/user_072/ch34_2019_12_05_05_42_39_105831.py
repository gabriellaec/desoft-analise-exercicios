a=float(input('Depósito Inicial: '))
b=float(input('Taxa de juros (decimal): '))
i=0
atual = a
while i < 24:
    print('{0:.2F}'.format(atual*(t+1)))
	atual*= (t+1)
    i+=1
print('{0:.2f}'.format(atual))