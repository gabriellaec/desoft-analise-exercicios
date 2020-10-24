def valor_conta(preco):
    A=preco*0.1
    return A
preco=int(input('Valor da conta?'))
print('Valor da conta com 10%: {0}'.format(float(valor_conta(preco))))