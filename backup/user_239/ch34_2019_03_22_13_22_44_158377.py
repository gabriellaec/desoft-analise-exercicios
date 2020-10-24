capital=float(input('Qual o depósito inicial?'))
taxa=float(input('Qual a taxa de juros?'))
inicial=capital
m=1
juros=taxa
while m<=24:
    ganho=juros*capital
    capital=capital+ganho
    m+=1 
    print('{0:.2f}'.format(capital))
print('O ganho total foi de R$ {0:.2f}'.format(capital-inicial))