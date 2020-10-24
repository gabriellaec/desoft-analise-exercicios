def pos_arroba(email):
    return email.find('@')

def nome_usuario(pos_arroba(email)):
    lista_email = email.split('@')
    nome_usuario = lista_email[0]
    return print(nome_usuario)