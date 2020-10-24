deposito=float(input('Qual foi o depósito inicial? '))
juros=float(input('Qual é a taxa de juros da poupança? '))
mes=1
saldo=deposito
while mes<=24:
    ganho=saldo*juros
    saldo=saldo+ganho
    print('Mês {0}: saldo {1:.2f}'.format(mes,saldo))
    mes+=1
ganhototal=saldo-deposito
print('O total ganho no período foi de {0:.2f} reais'.format(ganhototal))