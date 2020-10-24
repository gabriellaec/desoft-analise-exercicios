distancia = int(input("Quantos km o senhor deseja percorer? "))
if distancia < 200:
    dinheiro1 = 0.50*distancia
    print("Você gastara {} reais".format(dinheiro1))
else:
          dinheiro2 = 100 + 0.45*(distancia-200)
          print("Você gastara {} reais".formta(dinheiro2))