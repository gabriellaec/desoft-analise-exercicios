lista = []
soma = 0
i = 3
numero = int (input ('Escolha um número: '))      
    
while numero != 0:
	soma += numero
	lista.append (numero)
    numero = int (input ('Escolha um número: '))

print ('Soma é: {0}'. format (soma))
	