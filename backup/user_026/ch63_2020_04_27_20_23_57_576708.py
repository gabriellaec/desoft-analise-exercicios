def pos_arroba(string):
    for i in string:
        if i == '@':
            return string.index(i)

def nome_usuario(email):
    a= pos_arroba(string)
    usuario=texto[:a]
    return usuario
        