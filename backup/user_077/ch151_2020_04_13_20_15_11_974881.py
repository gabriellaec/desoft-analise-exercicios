def classifica_lista(lista):
    for e in lista:
        if lista[e]<lista[e+1]:
            return 'crescente'
        elif lista[e]>lista[e+1]:
            return 'decrescente'
        else:
            return 'nenhum'