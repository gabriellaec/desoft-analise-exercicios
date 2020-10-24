def nome_usuario(email):
    i = 0
    while i <len(email):
        if email[i] == '@':
            a = i
            i+=1
        else:
            i+=1 
    return email[ :arroba]