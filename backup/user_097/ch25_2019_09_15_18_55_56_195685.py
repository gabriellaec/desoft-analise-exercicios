def calcula_preco(distancia):
    if (distancia <= 200):
        preco = distancia*0.50
        return preco
    elif (distancia > 200):
        preco = 200*0.50
        preco = preco + (distancia-200)*0.45
        return preco