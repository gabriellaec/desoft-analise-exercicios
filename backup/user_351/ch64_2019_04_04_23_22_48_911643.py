def nome_usuario(email):
    i=0
    usuario =""
    while i<len(email):
        if email[i] != "@":
            usuario+=email[i]
        else:
            break
        i+=1
    return usuario