distancia = input("Qual a distância que o passageiro deseja percorrer?")
if distancia <=200:
    preco = 0.5 * distancia
if:
    preco = 100 + 0.45 * (distancia - 200)
    print("{0:.2f}".format(preco))
