def conta_a(palavra):
    contador = 0
    i = 0
    n = len(palavra)
    
    while i < n:
        if palavra[i] == 'a':
            contador += 1
        i += 1
    return contador
    
