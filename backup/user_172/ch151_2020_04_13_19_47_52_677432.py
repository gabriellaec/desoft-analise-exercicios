def classifica_lista(lista):
    n = len(lista)
    if n < 2:
        return 'nenhum'
    else:
        i = 0
        while i<n-1:
            if lista[i+1] > lista[i]:
                i+=1 
        return 'crescente'
            elif lista[i+1] < lista[i]:
                i+=1
        return 'decrescente'
            else:
                return 'nenhum'    
        