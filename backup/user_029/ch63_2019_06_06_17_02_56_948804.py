def pos_arroba(z):
    i = 0
    while i < len(z):
        if z[i] == "@":
            return i
        i+= 1