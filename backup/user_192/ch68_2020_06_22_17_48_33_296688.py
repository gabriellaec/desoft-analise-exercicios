def separa_trios(x):
    i = 0
    x = []
    while i < len(x):
        a = x[i:i+3]
        x.append(a)
        i += 3
    return x