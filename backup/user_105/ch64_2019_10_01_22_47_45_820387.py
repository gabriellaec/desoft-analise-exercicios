def pos_arroba(email):
    i = 0
    while i < len(email):
        if email[i]=='@':
            break
        else:
            i += 1
    return i
def nome_usuario(email):
    
    i = 0
    nome = email[ :pos_arroba(email):]       
        
   

    
    return nome