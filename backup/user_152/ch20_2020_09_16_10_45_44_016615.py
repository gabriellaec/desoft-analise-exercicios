def calcula_preco(km):
    if (km<=200):
        preco = km*0.5
    elif (km>200):
        d = km - 200
        preco = 200*0.5 + d*0.45
    return preco

distancia = float(input("Entre com a distancia percorrida: "))
valor = calcula_preco(distancia)
print(valor)
