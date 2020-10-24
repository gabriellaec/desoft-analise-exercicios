def verifica_lista(lista_numeros):
    for numero in lista_numeros:
        if numero %2 == 0:
            par = True
        else:
            impar = True
    if impar == True and par == False:
        return 'ímpar'
    if par == True and impar == False:
        return 'par'
    if impar and par:
        return 'misturado'