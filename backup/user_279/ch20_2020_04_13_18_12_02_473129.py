distancia = int(input("Quantos km o senhor deseja percorer? "))
if distancia < 200:
    dinheiro1 = 0.50*distancia
    print("Você gastara {} reais".format(dinheiro1)
elif distancia > 200:
    dinheiro2 = 100 + 0.45*(distancia-200)
    print("Você gastara {} reais".format(dinheiro2)