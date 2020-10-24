def eh_crescente(lista):
    posicao=1
    contador=1
    if len(lista)==0:
        return False
    maior=lista[0]
    while posicao<len(lista):
        if lista[posicao]>maior:
            maior=lista[posicao]
            contador+=1
        posicao+=1
    if len(lista)==contador:
        return True
    else:
        return False