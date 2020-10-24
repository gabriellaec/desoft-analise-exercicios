def classifica_lista(lista):
    for e in lista:
        if lista[e]<lista[e+1] and lista[e+1]<lista[e+2]:
            return 'crescente'
        elif lista[e]>lista[e+1] and lista[e+1]>lista[e+2]:
            return 'decrescente'
        else:
            return 'nenhum'