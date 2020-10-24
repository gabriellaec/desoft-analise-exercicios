def classifica_lista(lista1):
    if len(lista1) < 2:
        return ('nenhum')
    else:
        for i in lista1:
            if lista1[i]<lista1[i+1]:
                return ('crescente')
            if lista1[i]>lista1[i+1]:
                return ('decrescente')
            else:
                return ('nenhum')
    