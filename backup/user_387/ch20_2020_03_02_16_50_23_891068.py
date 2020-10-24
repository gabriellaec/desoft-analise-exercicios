distancia = float(input('Distância que deseja percorrer: '))

if distancia < 200:
    print(round(distancia * 0.5, 2))

else:
    print(round(distancia * 0.45, 2))