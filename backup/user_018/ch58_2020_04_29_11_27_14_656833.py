def conta_a(palavra):
    contador = []
    i = 0
    while i < len(palavra):
        if palavra[i] == 'a':
            contador.append(i)
        i+=1
    return len(contador)