def pos_arroba(email):
    contador=0
    posicao=0
    while contador <len(email):
        if email[contador]=="@":
            posicao=contador+1
        contador+=1

          
    return posicao