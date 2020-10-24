def pos_arroba(string):
    index = 0
    lista_string = list(string)
    for k in lista_string:
        index += 1
        if k == '@':
            pos = index - 1        
    return pos