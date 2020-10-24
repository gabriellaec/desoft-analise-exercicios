def pos_arroba(email):
    i = 0
    while i < len(email):
        if email[i]=='@':
            break
        else:
            i += 1
    return i
def nome_usuario(email):
    nome = ' '
    i = 0
    email[ :pos_arroba(email):]       
        
    nome = nome + email[i]
    i +=1
    return nome