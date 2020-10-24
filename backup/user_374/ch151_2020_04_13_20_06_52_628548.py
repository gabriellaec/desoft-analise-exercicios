def classifica_lista(lista):
    crescente = True
    decrescente = True
       
    if len(lista) < 1:
        return 'nenhum'
    
    for i in range(0,len(lista)):
        if i > 1:
            if lista[i] > lista[i-1] and lista[i-1] > lista[i-2]:
                crescente = True
                decrescente =  False
            
            elif lista[i] < lista[i-1]:
                crescente = False
                decrescente = True
            
    if crescente == True and decrescente == False:
        return 'crescente'
    elif decrescente == True and crescente == False:
        return 'decrescente'
    
    else:
        return 'nenhum'