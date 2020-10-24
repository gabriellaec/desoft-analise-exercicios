def nome_usuario(email):
    for i in email:
        if i=="@":
            return email[:i]
    

