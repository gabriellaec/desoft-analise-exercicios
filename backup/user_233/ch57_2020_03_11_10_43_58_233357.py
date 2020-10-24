def verifica_progressao(sequencia):
    
    pa = True
    pg = True
    
    incremento = []
    razao = []
    
    for i in range(1, len(sequencia)):
        incremento.append(sequencia[i] - sequencia[i - 1])
        razao.append(sequencia[i] / sequencia[i - 1])
    
    primeiro = incremento[0]
    
    for i in incremento[1:]:
        if i != primeiro:
            pa = False
            break
    
    primeiro = razao[0]

    for i in razao[1:]:
        if i != primeiro:
            pg = False
            break
    
    if pg and pa: return 'AG'
    if pg: return 'PG'
    if pa: return 'PA'
    else: 'NA'
        
        
        