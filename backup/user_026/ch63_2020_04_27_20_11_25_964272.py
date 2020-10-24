def nome_usuario(email,n):
    i=0
    
    while i<len(email):
        if i=='@':
            i=n
        else:
            break
        i+=1
    return email[:n]
        