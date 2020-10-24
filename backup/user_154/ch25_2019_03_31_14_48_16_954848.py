def preço(distancia):
    if distancia <= 200:
        return distancia*0.5
    return (distancia - 200)*0.45 + preço(200)

distancia = int(input("Distancia"))

print("O preço da sua passagem é R$ {0:.2f}".format(preço(distancia)))