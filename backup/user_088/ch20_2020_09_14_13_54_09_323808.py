distancia = int(input("Digite a distância a percorrer: "))
if (distancia <= 200):
    total = 0.5 * (distancia)
    print("%.2f" %total)
else:
    total = 0.45 * (distancia)
    print("%.2f" %total)