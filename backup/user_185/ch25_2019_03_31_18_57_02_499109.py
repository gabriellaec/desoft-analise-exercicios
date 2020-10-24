distancia_km = int(input("Qual foi a quilometragem percorrida em sua viagem? "))
if distancia_km < 200:
    print(distancia_km * 0,5)
else:
    print(199 * 0,5 + (distancia_km - 199)*0,45)

                   