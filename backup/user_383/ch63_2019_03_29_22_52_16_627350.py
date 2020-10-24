def pos_arroba(arroba):
    cont=0
    while cont<len(arroba):
        if arroba[cont]=='@':
            pos=cont
        cont+=1
    return pos