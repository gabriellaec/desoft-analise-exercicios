def classifica_lista(lista):
    
    # retorna 'nenhum' caso lista não seja grande o suficiente
    if len(lista) < 2: return 'nenhum'
    
    # com base na diferença entre o primeiro e último elemento, exclui a possibilidade de ser estritamente crescente ou decrescente
    variacao = lista[-1] - lista[0]
    
    # se o primeiro e último elementos forem iguais, retorna 'nenhum'
    if variacao == 0: return 'nenhum'
    
    if variacao > 0:    # lista possivelmente crescente
        
        elemento_anterior = lista[0]    # variável para comparar cada elemento ao anterior
        
        for elemento in lista[1:-1]:    # verifica se cada elemento é maior que o anterior
            if elemento <= elemento_anterior: return 'nenhum'
            elemento_anterior = elemento
        
        return 'crescente'
    
    if variacao < 0:    # lista possivelmente decrescente
        
        elemento_anterior = lista[0]    # variável para comparar cada elemento ao anterior
        
        for elemento in lista[1:-1]:    # verifica se cada elemento é menor que o anterior
            if elemento >= elemento_anterior: return 'nenhum'
            elemento_anterior = elemento
        
        return 'decrescente'
        