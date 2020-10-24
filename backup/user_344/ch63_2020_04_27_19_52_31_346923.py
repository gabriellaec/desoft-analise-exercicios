def pos_arroba(email):
    pos = -1
    i=0
    n = len(email) 
    while i < n:
        if email[i] == '@':
            pos = i
        i += 1
    return pos




def nome_usuario(email):
    pos = pos_arroba(email)
    return email[:pos]