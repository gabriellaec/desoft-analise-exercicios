def estritamente_crescente(x):
    x.sort()
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    j = y[0]
    k = []
    c = 1
    while c <= len(y):
        if y[c] >= j:
            k.append(y[c])
            c+=1
    return k
        