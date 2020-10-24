def eh_crescente(lista):
    v=0
    c=True
    for i in lista:
        if i>v:
            v=i
            return c
        else:
            c=False
    return c
                