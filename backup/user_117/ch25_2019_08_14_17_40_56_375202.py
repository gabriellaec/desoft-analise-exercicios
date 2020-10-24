distancia = int(input("Distância em km: "))

if  int (distancia) < 200:
    valor = int(distancia) * 0.5
elif int(distancia) > 200:
    valor = 100 + 0.45 * (int(distancia) - 200) 