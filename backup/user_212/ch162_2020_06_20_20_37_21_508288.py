def verifica_lista(lista):
    
    so_par = True 
    so_impar = True 
    
    if len(lista) == 0:
        return ("misturado")
    for n in lista:
        if n%2 == 0 :
            so_impar = False
        elif n%2 != 0:
            so_par = False 
            
    if so_par == True and so_impar == False:
        return ('par')
    elif so_par == False and so_impar == True:
        return ('ímpar')
    elif so_par == False and so_impar == False:
        return('misturado)
               