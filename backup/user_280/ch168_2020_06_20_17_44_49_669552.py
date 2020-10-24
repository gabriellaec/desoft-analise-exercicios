def login_disponivel(string, lista):
    i = 0
    j = 1
    while i < len(lista):
        while j < len(lista):
            if lista[i] == string:
                string += j
            else:
                j+=1
        i+=1  
    return string
            

            
        