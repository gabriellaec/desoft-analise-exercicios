def conta_a (s):
    i = 0
    contador = 0
    while i < len(s):
        if s[i] == 'a':
            contador = contador + 1
            i += 1
        return contador