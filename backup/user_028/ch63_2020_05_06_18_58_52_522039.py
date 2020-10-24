def pos_arroba(email):
    i = -1
    for e in email:
        i += 1
        if e == '@':
            pos = i
    return pos
def nome_usuario(email):
    pos = pos_arroba(email)
    return email[:pos]
    