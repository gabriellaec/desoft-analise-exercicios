def login_disponivel(string, lista):
    i = 0
    c = 0
    d = string
    while i < len(lista):
        if d == lista[i]:
            c+=1
            d = d[0:len(string)] + str(c)
        i+=1
    return d

            

            
        