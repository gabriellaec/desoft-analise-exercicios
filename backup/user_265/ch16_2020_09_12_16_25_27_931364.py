a = int (input ('Qual o valor da conta? '))
def porcento(x):
    y = x*1.1
    return y
certo = porcento(a)
print ('Valor da conta com 10%: R$ {0:.2f}' .format(certo))