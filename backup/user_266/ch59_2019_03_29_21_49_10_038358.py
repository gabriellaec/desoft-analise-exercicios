def conta_a(palavra):
    i=0
    contador = 0
    while i<len(palavra):
        if palavra[i] == 'a':
            contador+=1
        i+=1
    return contador