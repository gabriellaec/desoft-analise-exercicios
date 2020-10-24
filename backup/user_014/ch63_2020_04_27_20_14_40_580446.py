def pos_arroba(email):
    i = 0
    while i < len(email):
        if email[i] != '@':
            i += 1
        else:
            return i

def nome_usuario(email):
    i = pos_arroba(email)
    nome = [0::i]
    return nome