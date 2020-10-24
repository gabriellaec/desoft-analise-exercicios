def verifica_lista(n):
    par = list()
    impar = list()
    for i in n:
        if i%2 == 0:
            par.append(i)
        else:
            impar.append(i)
    if len(par) == 0 and len(impar) != 0:
        return 'impar'
    elif len(par) != 0 and len(impar) == 0:
        return 'par'
    else:
        return 'misto'