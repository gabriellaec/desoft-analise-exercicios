def quantos_uns(x):
    i = 0
    soma = 0
    
    while i < len(x):
        
        if x[i] == 1:
            soma += 1 
        i += 1
    return soma

print(quantos_uns(x))