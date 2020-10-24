def pos_arroba(email):
    pos = -1
    for i in range(len(email)):
        if email[i] == '@':
            pos= i
    return pos