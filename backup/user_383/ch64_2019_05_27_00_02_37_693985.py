def nome_usuario(email):
    i=0
    while i < len(email):
        if email[i] == '@':
            arroba = i
            nome = email[:arroba]
        i+=1
    return nome