def apaga_repetidos(t):
    i=0
    while i < len(t):
        if t.index[i] != t.index(t[i]):
            t[i] = '*'
        i += 1
    return t
        