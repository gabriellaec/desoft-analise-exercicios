def estritamente_crescente(x):
    i = 0
    r = []
    maior = 0
    for k in x:
        if x[i] > maior:
            r.append(x[i])
            maior = x[i]
        i = i + 1
    return r