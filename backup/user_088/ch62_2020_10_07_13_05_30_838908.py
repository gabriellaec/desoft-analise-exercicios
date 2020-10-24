def pos_arroba(palavra):
    i=0
    while(i<len(palavra)):
        if(palavra[i]=="@"):
            posicao=i
        i+=1
    return posicao