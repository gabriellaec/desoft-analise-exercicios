def nome_usuario(email):
    i = 0
    while i<len(email):
        if email[i] == '@':
            return email[:i]
            i += 1
        else:
            i += 1

        
        