def pos_arroba (email):
    pos = []
    for i in email:
        if i == '@':
            pos.append(i)
    return pos
