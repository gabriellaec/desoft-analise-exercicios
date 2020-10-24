def pos_arroba(string):
    pos = string.find('@')
    return pos

def nome_usuario(email):
    pos = pos_arroba(email)
    return(email[0:pos])