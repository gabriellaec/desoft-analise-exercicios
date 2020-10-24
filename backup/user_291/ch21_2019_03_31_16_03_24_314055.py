conta = float(input("Qual é o valor?: "))

def dez_porcento(valor):
    y = valor*1.1
    x = round(y, 2)
    return x


print(dez_porcento(conta))

