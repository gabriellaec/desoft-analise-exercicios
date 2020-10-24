def login_disponivel(string, lista):
    i = 0 
    c = 0
    d = string
    while i < len(lista):
        j = len(lista[i])
        if string == lista[i][0:j]:
            c += 1
            d = string + str(c)
        i += 1  
    return d