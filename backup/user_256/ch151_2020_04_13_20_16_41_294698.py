def classifica_lista(lista):
    t = 0
    t = lista[0]
    while len(lista)>=2:
        for elem in lista:
            if lista[elem] > t:
                t = lista[elem]
                return 'crescente'
            elif lista[elem] < t:
                return 'decrescente'
    else:
        return 'nenhum'
        
        