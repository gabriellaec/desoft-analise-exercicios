def classifica_lista(lista):
    i = 0
    while i < len(lista):
        if lista[i] < lista[i+1]:
        i += 1
            return("crescente")
        if lista[i] > lista[i+1]:
        i += 1
            return("decrescente")
        if len(lista)<2:
            return("nenhum")
    return lista