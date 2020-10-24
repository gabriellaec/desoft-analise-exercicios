def conta(x):
    y=x+0.1*x
    return y
a=float(input('valor da conta?'))
print("Valor da conta com 10%: R$ {0:.2f}".format(conta(a)))
