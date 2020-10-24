a=float(input('Qual o valor do depósito inicial? '))
b=float(input('Qual o valor da taxa de juros? '))
d=float(input('Qual o valor do depósito mensal? '))
b+=1
c=a*b
print('O valor da poupança nesse mês é {:.2f}'.format(c))
n=2
while n<=24:
        c+=d
        c=c*b
        e=c-a-d*23
        print('O valor da poupança nesse mês é {:.2f}'.format(c))
        n+=1
print('O total ganho com juros foi {:.2f}'.format(e))
    
        