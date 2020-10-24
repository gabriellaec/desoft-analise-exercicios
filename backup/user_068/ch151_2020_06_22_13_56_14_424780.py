def classifica_lista(lista):
    if len(lista)> 2:
        if lista[0] > lista[1]:
            for i in len(lista)-1:
                if  lista[i] < lista[i+1]:
                    return 'nenhum'
            return 'decrescente'
        if lista[0] < lista[1]:
            for i in len(lista)-1:
                if lista[i] > lista[i+1]:
                    return 'nenhum'
            return 'crescente'
    else:
        return 'nenhum'

