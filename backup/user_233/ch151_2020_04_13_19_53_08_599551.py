def classifica_lista(lista):
    
    if len(lista) < 2: return 'nenhum'
    
    variacao = lista[-1] - lista[0]
    
    if variacao == 0: return 'nenhum'
    
    if variacao > 0:    # possivelmente crescente
        
        elemento_anterior = lista[0]
        
        for elemento in lista[1:-1]:
            if elemento <= elemento_anterior: return 'nenhum'
            elemento_anterior = elemento
        
        return 'crescente'
    
    ir variacao < 0:    # possivelmente decrescente
        
        elemento_anterior = lista[0]
        
        for elemento in lista[1:-1]:
            if elemento >= elemento_anterior: return 'nenhum'
            elemento_anterior = elemento
        
        return 'decrescente'
        