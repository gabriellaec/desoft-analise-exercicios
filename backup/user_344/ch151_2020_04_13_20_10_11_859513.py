def classifica_lista(lista):
    if len(lista) <2:
        return 'nenhum'
    
    for i in lista:
        if lista == sorted(lista):
            return 'crescente'
        elif lista == sorted(lista, reverse = True):
            return 'decrescente'
        else:
            return 'nenhum'