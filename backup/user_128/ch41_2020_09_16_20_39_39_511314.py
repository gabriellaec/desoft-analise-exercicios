def zera_negativos(lista):

    i = 0

    while i < len(lista):

        if lista[i] < 0:
            lista[i] = 0

            i += 1

        else:
            i += 1
    print(lista)

lista = [0, 12, -13, 3, -4, 7]
zera_negativos(lista)