def pos_arroba(email):
    posicao=0
    i=0
    while email[i]!='@':
        posicao+=1
        i+=1
    return posicao

    