distancia = int(input('qual distância da viagem? '))
valor = 0
if distancia <= 200:
    valor = distancia*(1/2)
    print('{0:.2f}' .format(valor))
elif distancia > 200:
    valor = 100 + (distancia - 200)*0.45
    print('{0:.2f}'.format(valor))