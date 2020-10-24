def pos_arroba(email):
    pos = -1
    n = len(email)
    for i in n:
        if email[i] == '@':
            pos = i 
        return pos


def nome_usuario(email):
    pos = pos_arroba(email)
    return email[:pos]