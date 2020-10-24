def preco_da_passagem (preco,distancia,km):
    distancia = input("Qual a distância da corrida?")
    if distância <= 200:
        preco = distancia*0,50
    else:
        preco = distancia*0,45
    return preco