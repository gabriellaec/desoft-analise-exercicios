def verifica_progressao(sequencia):
    
    if len(sequencia) == 1: return 'NA'
    
    pg = True
    pa = True
    
    try: razao = sequencia[1] / sequencia[0]
    except ZeroDivisionError(): pg = False
    incremento = sequencia[1] - sequencia[0]
    
    for i in range(1, len(sequencia)):
        if sequencia[i] != sequencia[0] * razao ** i: pg = False
        if sequencia[i] != sequencia[0] + incremento * i: pa = False
    
    if pa and pg: return 'AG'
    if pa: return 'PA'
    if pg: return 'PG'
    else: return 'NA'
        
        
        
        