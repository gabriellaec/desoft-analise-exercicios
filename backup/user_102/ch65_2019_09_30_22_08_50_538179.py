def acha_bigramas(x):
    i = 0
    d = []

    while (i+1) < len(x):
        d.append(x[i:(i+2)])
        i += 1
    return d

