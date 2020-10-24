def pos_arroba(email):
    i = 0
    while i<len(email):
        if email[i] == '@':
            return i
        i += 1

def nome_usuario(em):
    return(em[:pos_arroba(em)+1])
