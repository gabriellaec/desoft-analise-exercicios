distancia_km = float(input("Qual foi a quilometragem percorrida em sua viagem? "))
if distancia_km < 200:
    print("{0:.2f}".format(distancia_km * 0.5))
else:
    print("{0:.2f}".format(100 + (distancia_km - 200)*0.45))