def pos_arroba(email):
    x = list(str(email))
    i = 0
    while i<len(x):
        if x[i]=='@':
            return i
        i += 1