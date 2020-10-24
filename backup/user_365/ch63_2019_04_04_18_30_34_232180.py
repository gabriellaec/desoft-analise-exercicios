def pos_arroba(mail):
    i=0
    while i<len(mail):
        if mail[i]=='@':
            posicao=i
        i+=1
    return posicao