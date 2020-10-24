def pos_arroba(x):
    y = list(x)
    i = 0
    j = 0
    while i <len(y):
        if y[i] == '@':
            j = i
    return j  