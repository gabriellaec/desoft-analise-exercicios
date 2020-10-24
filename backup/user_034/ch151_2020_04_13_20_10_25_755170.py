def classifica_lista(lista):
    if len(lista) < 2:
        return ("nenhum")
    elementos =lista[1]-lista[0]
    elif elementos>0:
        for e in range(len(lista) -1):
            if lista[e+1]-lista[e]<=0
            return ("nenhum")
    elif elementos<0:
        for e in range(len(lista) -1):
            if lista[e+1]-lista[e]>=0
            return ("nenhum")
    elif elementos == 0:
        return 'nenhum'
    elif elementos>0:
        return 'crescente'
    else:
        return 'decrescente'
