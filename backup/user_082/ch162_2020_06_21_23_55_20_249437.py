def verifica_lista(lista):
    par = False
    impar = False
    if len(lista) > 0:
        for i in lista:
            if i % 2 == 0:
                par = True
            if i % 2 != 0:
                impar = True

        if par and impar:
            return('misturado')
        elif par:
            return('par')
        elif impar:
            return('ímpar')
    else:
        return('misturado')