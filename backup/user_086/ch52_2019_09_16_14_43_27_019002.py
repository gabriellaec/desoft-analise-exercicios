def eh_crescente(lista):
    posicao=0
    contador=0
    maior=lista[0]
    while posicao<len(lista):
        if lista[posicao]>maior:
            maior=lista[posicao]
        posicao+=1
    if len(lista)==contador:
        return True
    else:
        return False
            