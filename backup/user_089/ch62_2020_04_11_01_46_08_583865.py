def pos_arroba(x):
    x = str(x)
    i = 0
    while i < x:
        if x[i] == '@':
            return i
        else:
            i = i + 1