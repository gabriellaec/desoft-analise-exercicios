def classifica_lista(lista1):
    if len(lista1) < 2:
        return ('nenhum')
    else:
        for i in range(len(lista1)):
            if lista1[i]<lista1[i+1] and lista1[i+1]<lista1[i+2]:
                return ('crescente')
            if lista1[i]>lista1[i+1]:
                return ('decrescente')
            else:
                return ('nenhum')
    