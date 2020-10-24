deposito_inicial = float(input('Qual o seu deposito inicial '))
taxa_juros = float(input('qual a taxa de juros ao mes '))
i = 0 

valor_total = deposito_inicial + deposito_inicial*taxa_juros

while i < 24:
    valor_total = valor_total + valor_total*taxa_juros
    i = i + 1
    print(' seu saldo é {0:.2f} reias'.format(valor_total))
print('seu lucro dps de 24 meses foi {0:.2f} reais'.format(valor_total))
    