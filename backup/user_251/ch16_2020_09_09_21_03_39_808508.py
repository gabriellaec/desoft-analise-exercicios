a = float(input("Qual o valor da sua conta? "))

def valor_da_conta(a):
    y = 1.1*a
    return y
print("Valor da conta com 10%: R$ {0:.2f}".format(valor_da_conta(a)))