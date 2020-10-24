def verifica_lista(lista):
    impar=True
    par=True
    for e in lista:
        if e%2!=0:
            par=False
        elif e%2==0:
            impar=False
    if impar and not par:
        return 'ímpar'
    elif not impar and par:
        return 'par'
    else:
        return 'misturado'