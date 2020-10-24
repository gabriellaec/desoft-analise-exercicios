def classifica_lista(lista):
    if len(lista)<2:
        return 'nenhum'
    else:
        if lista[0]<lista[1]:
            k = lista[0]
            crescente = True
            for i in range(len(lista)-1):
                if lista[i+1]>k:
                    continue
                else:
                    return 'nenhum'
        elif lista[0]>lista[1]:
            k = lista[0]
            decrescente = True
            for i in range(len(lista)-1):
                if lista[i+1]<k:
                    continue
                else:
                    return 'nenhum'
        else:
            return 'nenhum'
        if crescente:
            return 'crescente'
        elif decrescente:
            return 'decrescente'