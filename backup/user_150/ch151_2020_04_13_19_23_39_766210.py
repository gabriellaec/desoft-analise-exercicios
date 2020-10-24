def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    else:
        inicial = lista[0]
        for i in range(len(lista)-1):
            if lista[i+1] > inicial:
                inicial = lista[i+1]
                return 'crescente'
            elif lista[i+1] < inicial:
                inicial = lista[i+1]
                return 'decrescente'
            else:
                return 'nenhum'