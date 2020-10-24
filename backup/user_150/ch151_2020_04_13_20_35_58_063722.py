def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    else:
        inicial = lista[0]
        lista_crescente = [inicial]
        lista_decrescente = [inicial]
        for i in range(len(lista)-1):
            if lista[i+1] > inicial:
                inicial = lista[i+1]
                lista_crescente.append(lista[i+1])
            elif lista[i+1] < inicial:
                inicial = lista[i+1]
                lista_decrescente.append(lista[i+1])
        if lista == lista_crescente:
            return 'crescente'
        elif lista == lista_decrescente:
            return 'decrescente'
        else:
            return 'nenhum'