def classifica_lista (lista):
    i = 0
    while i < len(lista):
        if i > 2:
            if lista[i] < lista[i+1]:
                return 'crescente'
            elif lista[i] > lista[i+1]:
                return 'decrescente'
            else:
                return 'nenhum'
        else:
            return 'nenhum'