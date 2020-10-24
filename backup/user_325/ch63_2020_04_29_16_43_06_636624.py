def nome_usuario(email):
    i = 0
    while i < len(email):
        if "@" in email:
            print(email[0:[i]])
        i +=1
    return email
    