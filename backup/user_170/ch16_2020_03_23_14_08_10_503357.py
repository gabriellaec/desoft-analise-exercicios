v = float(input('Qual o valor da conta: '))
def gorjeta(v):
    g = v*1.1
    return g
print('Valor da conta com 10%: R$ {0:.2f}' .format(gorjeta(v)))