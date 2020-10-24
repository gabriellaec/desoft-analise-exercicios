def login_disponivel(string, lista):
    k = False
    j = 0
    for i in range(len(lista)):
        if string + j == lista[i]:
            j = int(j) + 1
            k = True
    if k:
        string = string + str(j)
        return string
    else:
        return string