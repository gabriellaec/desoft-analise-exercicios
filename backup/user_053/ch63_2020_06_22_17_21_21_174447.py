def pos_arroba(email):
    return email.find('@')

def nome_usuario(string):
    return string[:pos_arroba(string)]