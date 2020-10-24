v = float(input("Qual o valor da conta?"))

def valor_da_conta(v):
    v = 1.1*v
    return v
print("Valor da conta com 10%: R$ {0} ".format(v))