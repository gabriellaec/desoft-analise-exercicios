def nome_usuario(email):
    p = 0
    for l in range(len(email)):
        if l == '@':
            p=l
    usuario = email[:p]
    return usuario
            
        
        