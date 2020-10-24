def pos_arroba(email):
    i = 0
    pos = - 1
    while i < len(email): 
        if email[i] == "@":
            pos = i 
        i +=1
    return pos

def nome_usuario(email):
    juul = pos_arroba(email)
    return email[:juul]