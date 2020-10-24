def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    else:
        inicial = lista[0]
        crescente = False
        decrescente = False
        nenhum = False
        for i in range(len(lista)-1):
            if lista[i+1] > inicial:
                inicial = lista[i+1]
                crescente = True
            elif lista[i+1] < inicial:
                inicial = lista[i+1]
                decrescente = True
            else:
                nenhum = True
        if crescente:
            return 'crescente'
        elif decrescente:
            return 'decrescente'
        elif nenhum:
            return 'nenhum'