capital=float(input('Qual o depósito inicial?'))
taxa=int(input('Qual a taxa de juros?'))
inicial=capital
m=1
a=0
juros=taxa
while m<=24:
    ganho=juros*capital
    capital=capital+ganho
    a+=ganho
    m+=1 
    print('{1:.2f}'.format(capital))
print('O ganho total foi de R$ {0:.2f}'.format(capital-inicial))