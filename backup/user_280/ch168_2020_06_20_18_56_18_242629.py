def login_disponivel(string, lista):
    i = 0
    c = 0
    d = string
    #j = len(lista[i])
    while i < len(lista):
        if string == lista[i][:]:
            c+=1
            d = string + str(c)
        i+=1
    return d

            

            
        