def nome_usuario(email):
    i = 0
    while i<len(email):
        if email[i] == '@':
            return nome[:i]
        else:
            i += 1

        
        