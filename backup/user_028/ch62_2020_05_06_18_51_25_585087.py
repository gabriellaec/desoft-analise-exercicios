def pos_arroba(email):
    i = -1
    for e in email:
        i += 1
        if e == '@':
            pos = i
    return pos