def classifica_lista(lista):
    empty=[]
    for i in lista:
        if lista[i-1]<lista[i]:
            return 'crescente'
        if lista[i-1]>lista[i]:
            return 'decrescnete'
        if lista[i-1]==lista[i]:
            return 'nenhum'
        if lista==empty:
            return 'nenhum'
        else:
            return 'nenhum'