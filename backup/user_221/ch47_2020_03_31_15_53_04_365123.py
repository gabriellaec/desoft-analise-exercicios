def estritamente_crescente(x):
    a = []
    a[0] = x[0]
    i = 0
    while i < len(x):
        if x[i + 1] > x[i]:
            a.append(x[i + 1])
        i = i + 1    
    return a