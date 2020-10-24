def valor_conta(x):
    v= x+0.1*x
    return v
t= float(input('valor da conta?'))
print('Valor da conta com 10%: R$ {0:.2f}'.format(valor_conta(t))