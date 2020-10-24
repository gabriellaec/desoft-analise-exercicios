def valor_conta(preco):
    A=preco*0.1
    return A
preco=float(input('Valor da conta?'))
print('Valor da conta com 10%: R${0:.2f}'.format(float(valor_conta(preco))))