def valor_conta (c):
    v=c+(c*(1/10))
    return v
x=int(input('Qual o valor da conta? '))
y= valor_conta(x)
print ('{0:.2f}'.format(y))