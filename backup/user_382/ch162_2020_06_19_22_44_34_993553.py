def verifica_lista(lista):
    impar = False
    par = False
    
    for i in lista:
        if i % 2 =! 0:
            par = True
        else:
            impar = True
    
    if par and impar == True:
        return 'misturado'
    if par == True:
        return 'par'
    if impar = True:
        return 'ímpar'
            
    