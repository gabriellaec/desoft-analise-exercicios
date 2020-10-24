def verifica_lista(lista):
    if len(lista) == 0:
        return 'misturado'
    else:
        while i < len(lista):
            par = True
            impar = True
            if lista[i]%2 == 0:
                impar = False
                i+=1
            else:
                par = False
                i+=1
        if par == True:
            return 'par'
        elif impar == True:
            return 'ímpar'
        else:
            return 'misturado'