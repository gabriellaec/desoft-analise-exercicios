distancia = int(input("Qual distancia deseja percorrer? "))

def valor(distancia):
    if distancia<=200:
        valor1=distancia * 0.5
        return ("O valor sera de {0:.2f}".format(valor1))
    else:
        valor2=(distancia-200)* 0.45 + 100
        return ("O valor sera de {0:.2f}".format(valor2))

print(valor(distancia))