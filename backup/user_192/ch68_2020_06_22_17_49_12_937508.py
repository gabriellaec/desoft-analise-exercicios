def separa_trios(x):
    x = []
    i = 0
    while i < len(x):
        a = x[i:i+3]
        x.append(a)
        i += 3
    return x