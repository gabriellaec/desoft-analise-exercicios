def conta_a(texto):
    a = list()
    for i in len(texto):
        if texto[i] == 'a':
            a.append(texto[i])
    return len(a)