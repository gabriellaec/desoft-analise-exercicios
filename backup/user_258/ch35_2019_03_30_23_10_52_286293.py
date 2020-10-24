a=float(input('Qual o valor do depósito inicial? '))
b=float(input('Qual o valor da taxa de juros? '))
b+=1
c=a*b
print('O valor da poupança nesse mês é {:.2f}'.format(c))
n=2
while n<=24:
        d=float(input('Qual o valor do depósito mensal? '))
        c+=d
        c=c*b
        e=c-a
        n+=1
        print('O valor da poupança nesse mês é {:.2f}'.format(c))
print('O total ganho com juros foi {:.2f}'.format(e))
    
        