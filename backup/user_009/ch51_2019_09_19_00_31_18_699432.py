def estritamente_crescente(x):
    x.sort()
    y = []
    for i in x:
        if i not in y:
            y.append(i)
    return y 
        