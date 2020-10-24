def classifica_lista(lista):
    i = 0
    if lista[i+1] > lista[i]:
        while i <= len(lista):
            if lista[i+1] > lista[i]:
                i += 1
            else:
                break
            return 'crescente'
    elif lista[i+1] < lista[i]:
        while i <= len(lista):
            if lista[i+1] < lista[i]:
                i += 1
            else:
                break
            return 'decrescente'
    else:
        return 'nenhum'
        
            