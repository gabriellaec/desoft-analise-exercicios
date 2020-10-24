def separa_trios(lista):
    lista_trio = []
    for e in range(len(lista)):
        if (e + 1)%3 == 0:
            lista_trio.append(lista[(e - 2): (e + 1)])
    if len(lista)%3 != 0:
        if len(lista)%3 == 1 or len(lista) == 1:
            lista_trio.append(lista[-1]:)
        elif len(lista)%3 == 2 or len(lista) == 2:
            lista_trio.append(lista[-2: len(lista)])
    return lista_trio