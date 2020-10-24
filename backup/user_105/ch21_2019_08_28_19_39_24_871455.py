prato = float(input('qual o valor da comida: '))
def valor_comida(x):
    valor_total = x + (x*0.1)
    return valor_total
print('Valor da conta com 10%: R$ {0:.2f}'.format(valor_comida(prato)))