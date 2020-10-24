a=float(input('Qual o valor do depósito inicial? '))
b=float(input('Qual o valor da taxa de juros? '))
c=0
n=1
b+=1
while n<=24:
    d=(a+c)*b**n
    e=d-(a+c)
    n+=1
    c+=float(input('Qual o valor do depósito mensal? '))
    print('O valor da popupança nesse mês é {0:.2f}'.format(d))
print('O total ganho com juros é {0:.2f}'.format(e))  