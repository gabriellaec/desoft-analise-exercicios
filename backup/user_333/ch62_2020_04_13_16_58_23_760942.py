def pos_arroba(email):
    for i in range(len(email)):
        if email[i]=='@':
            posicao=i
            break
    return posicao
    