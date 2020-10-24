def soma_impares(x):
    soma_i = 0
    i = 0 
    while i < len(x):        
        if x[i]%2!=0:
            soma_i = Soma_i + x[i]
        i += 1
    return soma_i
            