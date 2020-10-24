def nome_usuario(email):
    pos=-1
    i=0
    n=len(email)
    for i in n:
        if email[i] == '@':
            pos=1
    return pos