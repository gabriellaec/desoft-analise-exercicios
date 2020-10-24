def pos_arroba (email):
    i = 0
    for i in range(len(email)):
        if email[i] == "@":
            return i
        
def nome_usuario (email):
    posicao = pos_arroba(email)
    t = email[:posicao]
    return t