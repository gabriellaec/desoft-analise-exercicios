def conta_a(palavra):
    contador=0
    for i in range(len(palavra)):
        if palavra[i] == 'a':
            contador+=1
    return contador