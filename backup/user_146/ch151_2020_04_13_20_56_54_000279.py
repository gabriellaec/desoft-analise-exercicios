def classifica_lista(lista1):
    i=0
    if len(lista1) < 2:
        return ('nenhum')
    else:
        while i<len(lista1):
            if lista1[i]<lista1[i+1]:
                return crescente
            else:
                if lista[i]>lista[i+1]:
                    return decrescente
                else:
                    return nenhum
        i+=1