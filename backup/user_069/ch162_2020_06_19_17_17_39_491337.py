def verifica_lista(lista):

    par = False
    impar = False

    for e in lista:

        if e % 2 == 0:
            par = True

        else:
            impar = True

    if par and impar or lista == []:
        return "misturado"

    elif par and not impar:
        return "par"

    else:
        return "ímpar"