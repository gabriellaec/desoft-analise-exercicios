def nome_usuario(email):
    contador=1
    posicao=0
    while contador<len(email):
        if email[contador]=="@":
            posicao=contador
        contador+=1
    return email[:posicao]
   	
        