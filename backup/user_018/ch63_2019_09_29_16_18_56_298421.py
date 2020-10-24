def pos_arroba (texto):
    i=0
    while i < len(texto):
        if texto[i]=='@':
            return i
    return i