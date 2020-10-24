def classifica_lista (lista):
    
    if len(lista) <2:
        r = 'nenhum'
        return r

    #condição inicial p/ iniciar os whiles
    decrescente = True
    crescente = True
    i=0
    while i< len(lista) -1: #Analisa se é decrescente
        j = i+1
        while j< len(lista)-2 and decrescente:
            if lista[i] > lista[j]:
                decrescente = True
                j+=1
            else:
                decrescente = False 
        i +=1
    
    i=0
    while i< len(lista) -1: #Analisa se é crescente
        j = i+1
        while j< len(lista)-2 and crescente:
            if lista[i] < lista[j]:
                crescente = True
                j+=1
            else:
                crescente = False 
        i +=1

    if crescente:
        r = 'crescente'
        return r
    if decrescente:
        r = 'decrescente'
        return r
    else:
        r = 'nenhum'
        return r