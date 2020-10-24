def classifica_lista(lista):
    n = len(lista)
    if n < 2:
        return 'nenhum'
    else:
        i = 0
        while i<n:
            if lista[i+1] > lista[i]:
                i+=1
                return 'crescente'
            if lista[i+1] < lista[i]:
                i+=1
                return 'decrescente'
            else:
                return 'nenhum'