def login_disponivel(nome,lista):
    a=len(nome)
    contador=0
    for ele in lista:
        if ele[:a]==nome:
            contador+=1
    contador=str(contador)
    if contador==0:
        return nome 
    else :
        return nome+contador