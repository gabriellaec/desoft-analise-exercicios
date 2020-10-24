def nome_usuario(email):
    while i< len(email):
        if email[i] == '@':
            return email[ : i]
    
