capital=float(input('Qual o depósito inicial?'))
juros=float(input('Qual a taxa de juros?'))
m=1

while m<=24:
    ganho=juros*capital
    capital=capital+ganho
    print('No mês {0}, o total ganho foi {1:.2f} reais'.format(m,ganho))
    m+=1
    

