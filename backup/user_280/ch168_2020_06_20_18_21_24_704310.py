def login_disponivel(string, lista):
    i = 0
    c = 0
    while i < len(lista):
        if lista[i] == string:
            c+=1
            indice += i
        i+=1
    if indice == 0:
        return string
    else:
        return string + str(indice)
            

            
        