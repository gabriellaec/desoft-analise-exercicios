def estritamente_crescente(lista):
    posicao=0
    if len(lista)==0:
        return 'Lista vazia'
    maior=lista[0]
    listamaiores=[maior]
    while posicao<len(lista):
        if lista[posicao]>maior:
            maior=lista[posicao]
            listamaiores.append(maior)
        posicao+=1
    return listamaiores