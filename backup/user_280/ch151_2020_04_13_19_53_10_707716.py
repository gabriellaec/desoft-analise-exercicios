def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    else:
        i = 0
        while i < len(lista) - 1:
            if lista[i+1] > lista[i]:
                i += 1
            else:
                return False
        return 'crescente'
        j=0
        while j < len(lista) - 1:
            if lista[j+1] < lista[j]:
                j += 1
            else:
                return 'nenhum'
        return 'decrescente'

            
                