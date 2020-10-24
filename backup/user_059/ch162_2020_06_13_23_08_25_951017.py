def verifica_lista(l):
    par = False
    impar = False
    for i in range(len(l)):
        if l[i]%2 == 0:
            par = True
        else:
            impar = True
    if par == True and impar == False:
        return 'par'
    elif par == False and impar == True:
        return 'impar'
    else:
        return 'misturado'
