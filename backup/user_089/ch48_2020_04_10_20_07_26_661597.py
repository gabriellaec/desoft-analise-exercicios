def eh_crescente(x):
    numero = True
    i = 0 
    while numero:
        while (i + 1) < len(x):
            
            if x[i] < x[i+1]:
                i = i + 1 
                return(True)
            
            else:
                numero = False
                return(False)
            
    