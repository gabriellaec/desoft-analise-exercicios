def pos_arroba(email):
    pos = -1
    for i in range(len(email)-1):
        if email[i] == '@':
            pos = i
    return pos