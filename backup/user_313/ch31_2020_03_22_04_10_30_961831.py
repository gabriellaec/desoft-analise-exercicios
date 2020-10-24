def eh_primo(x):
    if(x == 0 or x == 1):
        return(False)
    if (x == 2):
        return(True)
    if ( x > 0 and x % 2 == 0):
        contador = 2
        while contador < x:
            y = x/contador
            contador = contador - 1
            if (y == 0):
                return(False)

    
    else:
        return(True)

