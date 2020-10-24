def pos_arroba(x):
    posi = 0
    for i in range(len(x)):
        if x[i] == '@':
            posi = i
    return posi