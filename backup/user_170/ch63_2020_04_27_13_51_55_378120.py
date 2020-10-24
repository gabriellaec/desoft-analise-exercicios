def nome_usuario(email):
    p= 0
    for l in range(email)-1:
        if l == '@':
            p=l
    usuario = email[:p]
    return usuario
            
        
        