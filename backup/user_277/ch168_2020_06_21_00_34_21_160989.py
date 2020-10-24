def login_disponivel(string, lista):
    k = True
    j = 0
    for i in range(len(lista)):
        if string == lista[i]:
            j+=1
            j = str(j)
            string = string + j
    return string
        