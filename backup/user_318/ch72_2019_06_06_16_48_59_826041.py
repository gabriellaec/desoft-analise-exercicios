def lista_caracteres(n):
    a = n.split()
    for i in a:
        if i in a:
            del(i)
    return n
        