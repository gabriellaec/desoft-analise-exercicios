distancia = input("Distância em km: ")
if  distancia < 200:
    valor = distancia * 0.5
elif distancia > 200:
    valor = 100 + 0.45 * (distancia - 200) 