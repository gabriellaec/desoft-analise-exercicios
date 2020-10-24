 distancia = int(input("qual distância?"))
    if distancia > 200:
        valor = distancia*0.5 + (distancia - 200)*0.45
        return valor
    else:
        valor = 0.5*distancia
        return valor
    print(valor)
   