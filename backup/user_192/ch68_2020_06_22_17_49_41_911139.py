def separa_trios(x):
    z = []
    i = 0
    while i < len(x):
        a = x[i:i+3]
        z.append(a)
        i += 3
    return z