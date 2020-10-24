
v = float(input('Qual o valor da conta?:'))

def valor_da_conta(v):
    resultado = v * 1.1
    return resultado
print('Valor da conta com 10%: R$ {0:.2f}'.format(valor_da_conta(v)))

