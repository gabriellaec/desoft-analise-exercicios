a=int(input('Qual o depósito inicial? '))
b=int(input('Qual o valor da taxa de juros? '))
c=a*b**n
d=c-a
n=1
while n<=24:
    print('O valor da popupança nesse mês é {0:.2f}'.format(c))
    print('O total ganho com juros é {0:.2f}'.format(d))
    n+=1

    