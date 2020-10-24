def classifica_lista(lista):
    if len(lista)< 2:
        return 'nenhum'
    i = 0
    while i < len(lista):
        if lista[i] > lista[i+1]:
            return True
        if lista[i] < lista [i+1]:
            return False
        i+=1
    if True:
        return 'decrescente'
    if False:
        return 'crescente'
    if True and False:
        return 'nenhum'