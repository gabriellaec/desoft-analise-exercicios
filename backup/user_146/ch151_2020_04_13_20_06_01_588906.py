def classifica_lista(lista1):
    i=0
    if len(lista1) <= 2:
        return ('nenhum')
    else:
        if lista1[i]<lista1[i+1]:
            return ('crescente')
        if lista1[i]>lista1[i+1]:
            return ('decrescente')
        else:
            return ('nenhum')
    