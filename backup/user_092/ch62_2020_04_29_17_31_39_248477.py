def pos_arroba(x):
    i = 0
    while i <= len(x):
        if '@' in x:
            print x[i]
        i += 1
    return x