def pos_arroba(l):
    i = 0
    for e in l:
        if e == "@":
            return i
        i += 1