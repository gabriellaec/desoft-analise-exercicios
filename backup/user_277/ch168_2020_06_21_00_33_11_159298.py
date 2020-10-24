def login_disponivel(string, lista):
    k = True
    i = 0
    for i in range(len(lista)):
        if string == lista[i]:
            i+=1
            i = str(i)
            string = string + i
    return string
        