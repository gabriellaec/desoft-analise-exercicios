distancia_km = float(input("Qual foi a quilometragem percorrida em sua viagem? "))
if distancia_km <= 200:
    print(distancia_km * 0.5)
else:
    print(100 + (distancia_km - 200)*0.45)

                   