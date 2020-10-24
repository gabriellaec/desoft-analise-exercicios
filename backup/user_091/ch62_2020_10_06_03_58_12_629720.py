def pos_arroba(nome):
    i=0
    soma=0
    while i<len(nome):
        if nome[i]=='@':
            soma+=i
            i+=1
        else:
            i+=1
    return soma