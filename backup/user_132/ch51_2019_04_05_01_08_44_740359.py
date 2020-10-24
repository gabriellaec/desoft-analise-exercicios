def estritamente_crescente(x):
    i = 0
    r = []
    for k in x:
        if x[i] => x[i-1]:
            r.append(x[i])
        i = i + 1
    return r