def nome_usuario(email):
    pos=-1
    i=0
    n=len(email)
    while i<n:
        if email[i] == '@':
            pos=i
    retunr email[:pos]
        