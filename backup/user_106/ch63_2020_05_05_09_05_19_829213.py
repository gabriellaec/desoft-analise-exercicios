def pos_arroba(email):
    return email.find('@')

def nome_usuario(email):
    pos=def pos_arroba(email)
    nome=email[:pos]
    return nome
