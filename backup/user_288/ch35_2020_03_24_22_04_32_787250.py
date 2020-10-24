numero = int (input ('Escolha um número: '))
soma = 0
              
while numero != 0:
	soma += numero
	numero = int (input ('Escolha um número: '))
else:
	print ('Soma é: {0}'. format (soma))
	