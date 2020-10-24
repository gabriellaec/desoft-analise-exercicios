def classifica_lista(lista):
    i = 1
    c = 0
    d = 0
    if len(lista) < 2:
        return 'nenhum'
    while i < len(lista):
        if lista[i] > lista[i-1]:
            c += 1
            if c == len(lista) -1:
                return 'crescente'
        if lista[i] < lista[i-1]:
            d += 1
            if d == len(lista) -1:
                return 'decrescente'
        i += 1

    return 'nenhum'