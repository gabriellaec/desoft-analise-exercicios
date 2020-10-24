def pos_arroba (email):
    for i in range (len(email)):
        if email[i] == '@':
            return i     

def nome_usuario (email): 
    return email[:pos_arroba(email)]

