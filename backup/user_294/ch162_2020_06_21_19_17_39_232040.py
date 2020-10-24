def verifica_lista (lista):
    impar = 0
    par = 0
    for numeros in lista:
        if numeros%2 == 0:
            par +=1
        else:
            impar +=1
    if impar >0 and par == 0:
        return "ímpar"
    elif impar == 0 and par >0:
        return "par"
    else:
        return "misturado"
            