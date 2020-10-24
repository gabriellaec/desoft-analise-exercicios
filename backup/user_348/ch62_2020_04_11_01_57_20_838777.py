def pos_arroba(email):
    i = 0
    while i < len(email):
        if i == '@':
            return i
        i = i + 1
            