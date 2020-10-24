def conta_a(texto):
    a = list()
    i=0
    while i < len(texto):
        if texto[i] == 'a':
            a.append(texto[i])
            i+=1
    return len(a)