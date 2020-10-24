def eh_crescente(lista):
    i = 0
    c = True
    while i <len(lista):
        if lista[i] <= lista[i-1]:
            lista = False
            i = i + 1
        else:
            i = i + 1
    return c



    