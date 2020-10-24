def separa_trios(x):
    i = 0
    w = 0
    d = []
    while w < len(x):
        q = x[i:(i+3)]
        d.append(q)
        w += 1
        i += 3
    return d

