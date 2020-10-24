def login_disponivel(string, lista):
    k = True
    for i in range(len(lista)):
        if string != lista[i]:
            k = True
        else:
            k = False
    if k:
        return string
    else:
        a = string + '1'
        return a
        