def verifica_lista(lista):
    par=True
    impar=True
    for i in lista:
        if i%2==0:
            impar=False
        else:
            par=False
    if par and not impar:
        return "par"
    if impar and not par:
        return "ímpar"
    return "misturado"
        