def pos_arroba(arroba):
    cont=0
    while cont<len(arroba):
        if arroba[cont]=='@':
            pos=arroba[cont]
        cont+=1
    return cont