distancia_km = float(input("Qual foi a quilometragem percorrida em sua viagem? "))
if distancia_km <= 200.00:
    print(distancia_km * 0.50)
else:
    print(100.00 + (distancia_km - 200.00)*0.45)

                   