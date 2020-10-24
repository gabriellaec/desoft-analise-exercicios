def quantos_uns(x):
    i = 0
    soma = 0
    
    while i < len(x):
        i += 1 
        if x[i] == 1:
            soma += 1 
    return soma