def conta(x):
    y = 1.10*x
    return y

z = float(input('Qual o valor da conta?'))
valor_da_conta = conta(z)
print('Valor da conta com 10%: R$ {0:.2f}'.format(valor_da_conta))