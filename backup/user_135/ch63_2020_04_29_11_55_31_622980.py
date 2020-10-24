def pos_arroba(email):
    return email.find('@')

def nome_usuario(email):
    return email[:pos_arroba(email)]