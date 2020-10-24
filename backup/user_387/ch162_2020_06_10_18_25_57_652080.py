def verifica_lista(lis):
    par = False
    imp = False
    for i in lis:
        if i%2 == 0:
            par = True
        else:
            imp = True
            
    if par == True and imp == False:
        return 'par'
    if par == False and imp == True:
        return 'ímpar'
    if par == True and imp == True:
        return 'misturado'
    else:
        return 'misturado'
    
        