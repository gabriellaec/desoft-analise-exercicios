def verifica_lista(lista):
    PAR = False
    IMPAR = False
    MISTURADO = False

    if lista == []:
        MISTURADO = True
        return 'misturado'
    
    else:
        for i in lista:
            if i%2 == 0:
                PAR = True
            else:
                IMPAR = True

        if (PAR == True) and (IMPAR == True):
            return 'misturado'
        
        if (PAR == True) and (IMPAR == False):
            return 'par'
        if (PAR == False) and (IMPAR == True):
            return 'ímpar'