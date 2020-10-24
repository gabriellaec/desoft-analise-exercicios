di = float(input("Depósito inicial: "))
tjp = float(input("Taxa: "))
i=1
dep_inicial = di
juros = tjp
while i<=24:
    ganho = dep_inicial[i]*(juros/100)[i]
    print("O ganho foi de {0:.2f}".format(ganho))
    i+=1