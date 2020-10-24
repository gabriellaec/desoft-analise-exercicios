def pos_arroba(email):
    i = 0
    while i < len(email):
        if email[i] == '@':
            return i
        i = i + 1

def nome_usuario(email):
    f = pos_arroba(email)
    nome = email[0:f]
    return nome