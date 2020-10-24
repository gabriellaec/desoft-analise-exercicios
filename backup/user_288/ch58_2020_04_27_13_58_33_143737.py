def conta_a(palavra):
    contador = 0
    i= 0
    while i < len(palavra):
        if palavra[i] == 'a':
            contador += 1
        i += 1
        
    return contador