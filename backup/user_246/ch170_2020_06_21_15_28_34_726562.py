def apaga_repetidos(t):
    i=0
    t = list(t)
    while i < len(t):
        if i != t.index(t[i]):
            t[i] = '*'
        i += 1
    return (t)
        