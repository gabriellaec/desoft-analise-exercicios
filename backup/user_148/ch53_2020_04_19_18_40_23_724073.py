def soma_impares(n):
    i = 0
    soma = 0
    
    while i<len(n):
        if n[i]%2==1:
            soma = soma + n[i]
        i += 1
        
    return soma
