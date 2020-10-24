contador = 0
soma = 0

inicial = float(input('Qual o depósito inicial?'))
taxa_juros = float(input('Qual a taxa de juros? (em decimal)'))

while contador < 24:
    soma = inicial + inicial*taxa_juros
    contador += 1
    print ('{0:.2f}'.format(soma))
print ('{0:.2f}'.format(soma))