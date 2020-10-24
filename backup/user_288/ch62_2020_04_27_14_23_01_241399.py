def pos_arroba(email):
    pos = -1
    i = 0
    while i < len(email):
        if email[i] == '@':
            pos = i
        i += 1
    return pos