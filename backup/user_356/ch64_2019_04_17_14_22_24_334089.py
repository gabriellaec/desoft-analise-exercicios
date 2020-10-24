def nome_usuario(email):
    i=0
    tamanho=len(email)
    while i<tamanho:
        i+=1
        if email[i]=="@":
            return email[0:i]