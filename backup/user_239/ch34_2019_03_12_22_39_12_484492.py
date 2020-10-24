
capital=float(input('Qual o depósito inicial?'))
taxa=int(input('Qual a taxa de juros?'))

m=1
juros=taxa/100
while m<=24:
    ganho=juros*capital
    capital=capital+ganho
    print('No mês {0}, o saldo é de {1:.2f} reais'.format(m,capital))
    a+=ganho
    m+=1
print('O ganho total foi de {0:.2f}'.format(ganho))