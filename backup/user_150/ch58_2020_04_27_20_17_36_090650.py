def conta_a(string):
    contador = 0
    for i in range(len(string)):
        if string[i] == 'a':
            contador += 1
    return contador