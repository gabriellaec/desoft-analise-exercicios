def classifica_lista(lista):
    n = len(lista)
    if n < 2:
        return 'nenhum'
    else:
        i = 0
        while i<n+2:
            if lista[i+2]>lista[i+1] and lista[i+1]<lista[i] or lista[i+2]<lista[i+1] and lista[i+1]>lista[i]:
                i+=1
                #return 'nenhum'
            elif lista[i+1] > lista[i]:
                i+=1
                return 'crescente'
            elif lista[i+1] < lista[i]:
                i+=1
                return 'decrescente'
            
        return 'nenhum'
        
        