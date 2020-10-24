def eh_primo(x):
    if ( x % 2 == 0):
        contador = 2
        while contador < x:
            y = x/contador
            if (y == 0):
                return(False)
    
    else:
        return(True)

print(eh_primo(5))