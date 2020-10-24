di= float(input('qual foi o deposito inicial? '))
tj= float(input('qual a taxa de juros da poupança? '))
n=1
tj+=1
while n<=24:
    c= di*tj**n
    d= c-di
    n+=1
    print('O valor da poupança nesse mês é: {0:.2f}'.format(c))
print('O total ganho com juros é: {0:.2f}'.format(d))