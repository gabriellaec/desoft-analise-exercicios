def classifica_lista(lista):
    u=len(lista)
    n=lista[u-1]
    if n<2:
        return nenhum
    else:
        if lista[0]<lista[n]:
            return crescente
        else:
            if lista[0]>lista[n]:
                return decrescente
            