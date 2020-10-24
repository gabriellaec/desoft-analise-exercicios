def pos_arroba(email):
    for letra in email:
        if letra == '@':
            return email.index(letra)

def nome_usuario(email):
    pos = pos_arroba(email)
    return email[:pos]