def verifica_lista(lista):
    par = True
    impar = False
    if lista == "":
        return "misturado"
    for i in lista:
        if i % 2 == 0:
            impar = False
        else:
            par = False
    if impar:
        return "ímpar"
    elif par:
        return "par"
    else:
        return "misturado"