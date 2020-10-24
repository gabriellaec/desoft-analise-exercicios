def eh_crescente (lista):
    i = False
    if(len(lista) < 1):
        return(lista)
    contador = lista[0]
    for e in lista:
        if (e > contador):
            i = True
            contador = e
        else:
            i = False
            break
    return(i)

            