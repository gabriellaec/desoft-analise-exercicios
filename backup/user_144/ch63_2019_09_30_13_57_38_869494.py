def pos_arroba(email):
    pos = -1
    for i in len(email):
        if email[i] == '@':
            pos = i 
    return pos
