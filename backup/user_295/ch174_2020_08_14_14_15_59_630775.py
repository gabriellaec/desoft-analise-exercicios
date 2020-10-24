def imprime_tipo(n):
    if n % 3 == 0 and n % 5 != 0:
        return(print ("Tipo A"))
    elif n % 5 == 0 and n % 3 != 0:
        return(print ("Tipo B"))
    elif n % 3 == 0 and n % 5 == 0:
        return(print ("Tipo C"))
    elif n % 3 != 0 and n % 5 != 0:
        return(print ("Tipo D"))
        
        
        