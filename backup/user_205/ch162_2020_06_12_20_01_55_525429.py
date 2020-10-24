def verifica_lista(lista):
    teste = []
    PAR = True 
    IMPAR = True 
    for i in lista:
        if i%2 == 0:
            IMPAR = False
        elif i%2 != 0:
            PAR = False
    if PAR:
        return "par"
    elif IMPAR:
        return "impar"
    else:
        return "misturado"