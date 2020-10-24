
def calcula_conta(x):
    y=x*1.1
    return y
a=float(input("Valor da conta: "))
b=calcula_conta(a)
print('Valor da conta com 10%: R$ {0:.2f}'.format(b))
