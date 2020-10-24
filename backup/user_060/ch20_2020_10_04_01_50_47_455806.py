 distancia = input("qual distância?\n")
    if distancia <= 200:
        valor = 0.5*distancia
        return valor
    elif distancia > 200:
        valor = distancia*0.5 + (distancia - 200)*0.45
        return valor
    print(valor)
   