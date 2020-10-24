def pos_arroba(email):
    return email.find('@')
def nome_usuario(email):
    k=''
    for i in range(pos_arroba(email)):
        k+=email[i]
    return k