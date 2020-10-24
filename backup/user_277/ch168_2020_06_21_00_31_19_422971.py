def login_disponivel(string, lista):
    k = True
    for i in range(len(lista)):
        if string == lista[i]:
            string = string + i
    return string
        