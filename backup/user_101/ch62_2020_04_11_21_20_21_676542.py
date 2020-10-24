def pos_arroba(email):
    i = 0
    arroba = True
    while arroba:
        if email[i] != '@':
            i += 1
            arroba = True
        else:
            arroba = False
            return i
        