def login_disponivel(string, lista):
    k = True
    j = 0
    for i in range(len(lista)):
        if string == lista[i]:
            j = int(j) + 1
    string = string + str(j)
    return string
        