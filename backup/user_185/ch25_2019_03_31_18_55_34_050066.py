distancia_km = int(input("Qual foi a quilometragem percorrida em sua viagem? "))
def preço_passagem(distancia_km):
    if distancia_km < 200:
        return distancia_km * 0,5
    else:
        return 199 * 0,5 + (distancia_km - 199)*0,45
print(preço_passagem(distancia(km))
                   