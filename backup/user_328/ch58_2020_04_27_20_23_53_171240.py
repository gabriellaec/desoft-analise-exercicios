def conta_a(string):
    contador= 0 #conta os 'a' da palavra
    i= 0 #conta o indice da palavra
    while i < len(string):
        if string[i] == 'a':
            contador += 1
        i += 1
    return contador