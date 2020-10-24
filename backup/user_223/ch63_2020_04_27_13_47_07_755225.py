def nome_usuario(email):
    i=0
    while i < len(email):
        if email[i]=="@":
            posicao = i
            i+=1
        else:
            i+=1
    return email[:posicao]