x = input("informe o valor da conta: ")

def valor_da_conta(x):
    f = x*1.10
    return f

print("Valor da conta com 10%: {f}".format(f, prec=2))