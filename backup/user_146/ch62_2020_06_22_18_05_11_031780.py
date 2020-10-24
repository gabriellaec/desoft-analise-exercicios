def pos_arroba (email):
    pos = []
    for i in email[0]:
        if i == '@':
            pos.append(i)
    return pos
