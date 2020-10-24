def login_disponivel(string, lista):
    i = 0
    while i < len(lista):
        j = 1
        newstr = ''
        while j < len(lista):
            if lista[i] == string:
                string += str(j)
            else:
                j+=1
        i+=1  
    return string
            

            
        