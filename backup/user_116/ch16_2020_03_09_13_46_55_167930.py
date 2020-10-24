def valor(a):
    v=a+(a*(10/100))
    return(v)
a=float(input("qual o valor da sua conta?"))
print("Valor da conta com 10%: R$ {0:.2f}".format(valor(a)))