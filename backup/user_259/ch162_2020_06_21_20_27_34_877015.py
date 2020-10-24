def verifica_lista(lista):
    par = 0
    impar = 0
    if len(lista) == 0:
        return 'misturado'
    else:
        for n in lista:
            if n%2 == 0:
                par += 1
            elif n%2 == 1:
                impar += 1
        if par > 0 and impar == 0:
            return 'par'
        elif par == 0 and impar > 0:
            return 'impar'
        else:
            return 'misturado'
            