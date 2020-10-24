def login_disponivel(string, lista):
    i = 0
    c = 0
    j = len(lista[i])
    d = string
    while i < len(lista):
        if string == lista[i][0:j]:
            c+=1
            d = string + str(c)    
        i+=1
    return d

            

            
        