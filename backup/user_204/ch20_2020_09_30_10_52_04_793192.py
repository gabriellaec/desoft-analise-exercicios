distancia = int(input("Qual a distância? "))
if distancia <= 200:
    valor = distancia * 0.50
    print("Valor {0:.2f}".format(valor))
else:
    inteiro = distancia - 200
    valorextra = inteiro * 0.45 + 100
    print("Valor {0:.2f}".format(valorextra))