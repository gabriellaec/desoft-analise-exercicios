def pos_arroba(email):
    for i in range(len(email)):
        if email[i] == '@':
            return i

def nome_usuario(email):
    pos = pos_arroba(email)
    return email[: pos]