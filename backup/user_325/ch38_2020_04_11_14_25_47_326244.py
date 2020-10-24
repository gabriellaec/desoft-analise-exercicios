def quantos_uns(x):
    i = 0
    s = 0
    while i < len(x):
        if x[i] == 1:
            s += 1
        i += 1
    return s
        