valor= float(input("conta:"))
def função_10(valor):
    y= round (valor*1.1)
    return y
y=função_10(valor)
print ("Valor da conta com 10%: R$ {0:.2f}" .format(y))