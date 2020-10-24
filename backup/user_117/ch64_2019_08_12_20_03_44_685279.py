def nome_usuario(email):
    i=0
    while i<len(email):
        if email[i] == '@':
            i += 1
            return email [0:i] 
    