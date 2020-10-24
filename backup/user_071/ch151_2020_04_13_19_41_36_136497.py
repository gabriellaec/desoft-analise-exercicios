def classifica_lista(lista):
    if lista==[]:
        return 'nenhum'
    for i in lista:
        if lista[i-1]<lista[i]:
            return 'crescente'
        if lista[i-1]>lista[i]:
            return 'decrescente'
        if lista[i-1]==lista[i]:
            return 'nenhum'
        else:
            return 'nenhum'