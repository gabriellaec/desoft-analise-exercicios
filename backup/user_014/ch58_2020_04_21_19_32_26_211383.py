def conta_a (s):
    i = 0
    contador = 0
    while i < len(s):
        if s[i] != 'a':
            i += 1
            contador = 0
        else:
            i += 1
            contador += 1 
        return contador