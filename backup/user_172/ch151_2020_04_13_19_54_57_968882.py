def classifica_lista(lista):
    n = len(lista)
    if n < 2:
        return 'nenhum'
    else:
        i = 0
        while i<n-1:
           
            while lista[i+1] > lista[i]:
                i+=1
                return 'crescente'
            while lista[i+1] < lista[i]:
                i+=1
                return 'decrescente'
            
            return 'nenhum'
        
        