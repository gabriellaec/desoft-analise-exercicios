a=float(input('Qual o valor do depósito inicial? '))
m=float(input('Qual o valor do depósito mensal? '))
b=float(input('Qual o valor da taxa de juros? '))
n=1
b+=1
c = a
while n<=24:
    c=c*b + m
    n+=1
    print('O valor da popupança nesse mês é {0:.2f}'.format(c))
print('O total ganho com juros é {0:.2f}'.format(c-a-24*m))  