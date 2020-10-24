def pos_arroba(a):
    i = 0 
    x = 0
    while i < len(a):
        if a[i] == "@":
            x = i
    return x