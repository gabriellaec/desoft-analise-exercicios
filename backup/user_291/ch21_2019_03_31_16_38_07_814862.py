conta = float(input("Qual é o valor?: "))

def dez_porcento(valor):
    y = valor*1.1
    return y

valor = dez_porcento(conta)

print("sua conta deu {0:.2f}".format(valor))

