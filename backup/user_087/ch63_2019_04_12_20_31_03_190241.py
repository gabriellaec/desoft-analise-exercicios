def pos_arroba(x):
    i = 0
    while i < len(x):
        if x[i] == '@':
            break
        i += 1
    return i