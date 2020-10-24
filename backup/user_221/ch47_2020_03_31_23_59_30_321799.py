def estritamente_crescente(x):
    a = []
    if x == []:
        return x
    a.append(x[0])
    maior_numero = x[0]
    i = 1
    while i < len(x):
        if x[i] > maior_numero:
            a.append(x[i])
            maior_numero = x[i]
        i = i + 1    
    return a