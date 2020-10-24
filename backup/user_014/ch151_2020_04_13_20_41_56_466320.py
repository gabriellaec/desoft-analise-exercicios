def classifica_lista(lista):
    if lista == []:
        return 'nenhum'
    elif len(lista) < 2:
        return 'nenhum'
    i = 0
    while i < len(lista):
        if lista[i] < lista[i+1]:
            return 'crescente'
            if lista[i+1] > lista[i+2]:
                return 'nenhum'
            else:
                return 'crescente'
        elif lista[i] > lista[i+1]:
            return 'decrescente'
            if lista[i+1] < lista[i+2]:
                return 'nenhum'
            else:
                return 'decrescente'
        else:
            return 'nenhum'
        i += 1