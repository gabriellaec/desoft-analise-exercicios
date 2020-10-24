def separa_trios(x):
    i = 0
    d = []
    while i < len(x):
        q = x[i:(i+3)]
        d.append(q)
        i += 3
    return d