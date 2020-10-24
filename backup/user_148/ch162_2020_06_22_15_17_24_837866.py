def verifica_lista(num):
    if len(num) == 0:
        return 'misturado'
   
    par = True
    impar = True
    
    for n in num:
        if n % 2 == 1:
            par = False
        if n % 2 == 0:
            impar = False
            
    if par:
        return 'par'
    elif impar:
        return 'ímpar'
    else:
        return 'misturado'
