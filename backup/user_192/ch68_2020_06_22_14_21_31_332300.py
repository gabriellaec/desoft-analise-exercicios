def separa_trios(x):
    i = 0
    x = []
    y = []
    while i < len(x):
        a = x[:3]
        y.append(a)
        x.append(y)
        i += 1
    return x