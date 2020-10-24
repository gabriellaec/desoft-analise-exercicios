def pos_arroba(palavra):
    i = 0
    p = 0
    while i < len(palavra):
        if palavra[i] == '@':
            p = i
        i+=1
    return p
        