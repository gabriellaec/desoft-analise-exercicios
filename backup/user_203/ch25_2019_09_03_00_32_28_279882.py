distancia = float(input( 'Quantos km voce percorre ? '))
valor1=distancia*0.5
valor2=(distancia-200)*0.45+100

if distancia<=200:
	print('O valor da passagem eh: {0:.2f}'.format(valor1))
else:
    print(' O valor da passagem eh: {0:.2f}'.format(valor2))
    
