distancia = input("Distância em km: ")
if  int (distancia) < 200:
    valor = int(distancia) * 0.5
elif distancia > 200:
    valor = 100 + 0.45 * (distancia - 200) 