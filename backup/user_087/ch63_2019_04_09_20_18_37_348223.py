def pos_arroba(x):
    i = 0
    while i < len(x):
        if x[i] == '@':
            i += 1
    return i+1