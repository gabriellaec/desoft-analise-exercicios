def pos_arroba(email):
    i = 0
    p = 0
    while i < len(email):
        p += 1
        i += 1
        if email[i] == '@':
            return p