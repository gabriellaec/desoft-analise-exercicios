def pos_arroba(texto):
    pos : -1
    i = 0
    n = len(texto)
    while i < n :
        if texto[i] == '@':
            pos = i
        i+=1
    return pos
    