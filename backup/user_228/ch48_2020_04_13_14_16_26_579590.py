def eh_crescente(lista):
    v=0
    c=True
    for i in lista:
        if i>v:
            v=i
        else:
            c=False
    return c
                