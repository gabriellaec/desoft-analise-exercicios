listamaiores=[]
def estritamente_crescente(lista):
    posicao=0
    maior=lista[0]
    while posicao<len(lista):
        if lista[posicao]>maior:
            maior=lista[posicao]
            listamaiores.append(maior)
        posicao+=1
    return listamaiores