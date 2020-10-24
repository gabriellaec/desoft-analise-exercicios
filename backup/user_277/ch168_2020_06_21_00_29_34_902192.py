def login_disponivel(string, lista):
    k = True
    for i in range(len(lista)):
        if string != lista[i]:
            k = True
        else:
            string = string +'1'
    if k:
        return string
    else:
        return string
        