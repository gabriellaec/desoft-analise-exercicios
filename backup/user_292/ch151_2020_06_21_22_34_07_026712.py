def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    C = lista[0]
    D = lista[0]
    for i in lista:
        if i>C:
            C+=i
            return 'crescente'
        if i<C:
            return 'nenhum'
        if i<D:
            D+=i
            return 'decrescente'
        elif i>D:
            return 'nenhum