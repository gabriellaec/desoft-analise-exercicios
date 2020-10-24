def verifica_lista(lista):

    impar = True
    par = True
  

    for numero in lista:
        if numero %2 != 0 and par == True:
            par = False
        
        elif numero %2 == 0 and impar = True:
            impar = False

    
    if impar == True and par == False:
        return 'ímpar'
    
    elif impar == False and par == True:
        return 'par'

    else:
        return 'misturado'