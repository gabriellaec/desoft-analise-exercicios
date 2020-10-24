def pos_arroba(x):
    i = 0
    while i <= len(x):
        if '@' in x:
            return x[i]
        i += 1