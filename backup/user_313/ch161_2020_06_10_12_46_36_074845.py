import math

def PiWallis(x):
    
    lista_par = list()
    lista_impar = list()
    lista_impar.append(1)
    

    contador = 0
    par = 2
    impar = 3

    while True:
        lista_par.append(par)
        lista_impar.append(impar)
        
        contador += 1

        if impar == 1:
            impart += 2
            
        if contador % 2 == 0:
            par += 2
            impar += 2
            
        if contador >= x:
            break
    
    pi = lista_par[0]/lista_impar[0]    
    for t in range(len(lista_par)-1):
        pi *= lista_par[t+1]/lista_impar[t+1]
        
    
    return pi*2