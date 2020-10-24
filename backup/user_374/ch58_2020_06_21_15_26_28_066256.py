def conta_a(string):
    contador = 0
    for i in string.lower():
        if i == 'a':
            contador += 1
    
    return contador
