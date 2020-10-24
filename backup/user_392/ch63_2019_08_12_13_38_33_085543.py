def pos_arroba (email):
    i = 0
    n = len(email)
    pos = 0
    while i < n:
        if email[i] == '@':
            pos = i
    return pos