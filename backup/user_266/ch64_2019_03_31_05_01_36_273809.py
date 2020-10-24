def nome_usuario(email):
    i=0
    nome=''
    while i<len(email):
        if email[i]!='@':
            nome+=email[i]
        else:
            break
        i+=1
    return nome