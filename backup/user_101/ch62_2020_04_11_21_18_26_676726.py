def pos_arroba(email):
    arroba = True
    while arroba:
        if email[i] != '@':
            arroba = True
        else:
            arroba = False
            return email[i]
        