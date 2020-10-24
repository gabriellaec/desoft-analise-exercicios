def nome_usuario(email):
    i=0
    usuario =""
    while i<len(email):
        if email[i] != "@":
            usuario.append(email[i])
        else email[i] == "@":
            break
        i+=1
    return usuario
        
         
            
           
        