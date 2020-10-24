def pos_arroba(nome):
    i=0
    soma=0
    while i<len(nome):
        if nome[i]=='@':
            soma+=i+1
            i+=1
        else:
            i+=1
    return soma