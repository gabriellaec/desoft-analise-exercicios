deposito_inicial = float(input('Qual o seu deposito inicial '))
taxa_juros = float(input('qual a taxa de juros ao mes '))
adição_mes_a_mes = float(input('qual a adiiçao por mes '))
i = 0 

valor_total = deposito_inicial + deposito_inicial*taxa_juros
#print(' seu saldo é {0:.2f} reias'.format(valor_total))
while i < 24:
    valor_total = valor_total + valor_total*taxa_juros
    valor_total = valor_total + adição_mes_a_mes
    print(' seu saldo é {0:.2f} reias'.format(valor_total))
    i = i + 1

print('seu lucro dps de 24 meses foi {0:.2f} reais'.format(valor_total-deposito_inicial))
    