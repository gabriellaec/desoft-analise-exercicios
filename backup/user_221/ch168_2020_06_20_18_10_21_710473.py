def login_disponivel(string, lista):
    i = 0
    j = len(string)  
    c = 0
    while i < len(lista):
        if string == lista[i][0:j]:
            c += 1
            d = string + str(c)
        else:
            d = string
        i += 1
    return d