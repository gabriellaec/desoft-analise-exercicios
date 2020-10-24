deposito=float(input('Quanto de depósito? '))
juros=float(input('Qual a taxa de juros? '))

mes = 1
soma = 0

while mes != 25:
    deposito=(deposito*(juros/100))+deposito
    lucro=(deposito*(juros/100)+deposito)-deposito
    soma+=lucro
    print('Mês {}: {:.2f} reais!'.format(mes, deposito))
    mes+=1
print('Total lucro: {:.2f}!'.format(soma))
