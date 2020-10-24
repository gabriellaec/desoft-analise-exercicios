dep = float(input("deposito "))
juros = float(input("Juros "))
i = 0
soma = 0
while(i < 24):
    ganho = dep * juros
    dep += juros
    soma += ganho
    i += 1
    print("Seu ganho foi {0:.2f}".format(ganho))

print("{hahaha 0:.2f}".format(soma))