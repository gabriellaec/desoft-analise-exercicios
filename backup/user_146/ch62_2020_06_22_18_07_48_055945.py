def pos_arroba (email):
    pos = []
    i = 0
    n = len(email)
    while i < n:
        if i == '@':
            pos.append(i)
    return pos