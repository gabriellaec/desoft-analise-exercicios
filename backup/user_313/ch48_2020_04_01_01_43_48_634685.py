def eh_crescente(l1):
    if len(l1) == 0:
        return l1
    a = len(l1)
    contador = 0

    while contador != a-1:

        if l1[contador+1]>=l1[contador]:
            contador = contador + 1

        else:
            return False

    return True