def classifica_lista(lista):
    for i in lista:
        if lista[i]<lista[i+1]:
            return 'crescente'
        if lista[i]>lista[i+1]:
            return 'decrescnete'
        if lista==[]:
            return 'nenhum'
        else:
            return 'nenhum'