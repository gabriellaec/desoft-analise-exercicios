def valor_conta (c):
    v=c+(c*(1/10))
    return v
x=int(input('Qual o valor da conta? '))
y= valor_conta(x)
print ('Valor da conta com 10%: R$ ''{0:.2f}'.format(y))
