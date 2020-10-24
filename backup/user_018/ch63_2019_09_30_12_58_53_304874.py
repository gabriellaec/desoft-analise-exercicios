def pos_arroba (texto):
    i=0
    while i < len(texto):
        if texto[i]=='@':
            print (i)
        i+= 1
    return i