def mais_populoso(x):
    dec = {}
    for i, e in x.items():
        f = 0
        for key, values in e.items():
            f = values + f
        dec[i] = f
        t = 0
    for keys, values in dec.items():
        if t < values:
            t = values
    for k, l in dec.items():
        if t == l:
            return(k)