def login_disponivel(string, lista):
    i = 0
    c = 0
    d = string
    while i < len(lista):
        if string == lista[i][0:len(lista[i])):
            c+=1
            d = string + str(c)    
        i+=1
    return d

            

            
        