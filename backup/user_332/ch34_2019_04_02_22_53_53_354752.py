dep = float(input("deposito "))
juros = float(input("Juros "))
i = 0
while(i < 24):
    ganho = dep * juros
    dep += juros
    i += 1
    print("Seu ganho foi {0:.2f}".format(ganho))