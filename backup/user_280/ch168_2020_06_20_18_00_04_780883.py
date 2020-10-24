def login_disponivel(string, lista):
    i = 0
    indice = 0
    while i < len(lista):
        j = 1
        while j < len(lista):
            if lista[i] == string:
                indice = j
            j+=1
        i+=1
    if indice == 0:
        return string
    else:
        return string + str(indice)
            

            
        