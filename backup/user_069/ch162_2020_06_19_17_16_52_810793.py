def verifica_lista(lista):

    par = False
    impar = False

    for e in lista:

        if e % 2 == 0:
            par = True

        else:
            impar = True

    if par and impar:
        return "misturado"

    if par and not impar:
        return "par"

    else:
        return "ímpar"