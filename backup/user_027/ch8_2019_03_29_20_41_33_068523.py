def verifica_PA(x):
    if len(x) == 1:
        return True
    razao = x[1] - x[0]
    for i in range(1,len(x)):
        if x[i] - x[i-1] != razao:
            return False
    return True

def verifica_PG(x):
    razão = x[1]/x[0]
    if len(x) == 1:
        return True
    for i in range(1,len(x)):
        if x[i]/x[i-1] != razão:
            return False
    return True

def verifica_progressao(x):
    if verifica_PA(x) and verifica_PG(x):
        return 'AG'
    if verifica_PA(x):
        return 'PA'
    elif verifica_PG(x):
        return 'PG'
    else:
        return 'NA'
    
