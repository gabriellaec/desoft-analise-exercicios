def pos_arroba(email):
    i = 0
    while email[i] != '@':
        i += 1
    return i

def nome_usuario(email):
    a = pos_arroba(email)
    nome = email[0:a]
    return nome