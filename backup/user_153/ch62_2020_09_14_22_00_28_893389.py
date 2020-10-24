def pos_arroba(email):
    for idx,c in enumerate(email):
        if c == '@':
            return idx