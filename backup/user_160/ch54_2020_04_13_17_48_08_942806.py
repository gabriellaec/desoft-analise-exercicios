def calcula_fibonacci(n):
    lista = []
    lista[0] = 1
    lista[1] = 1
    i = 2
    if n < 1:
        return (n)
    elif n < 2:
        return (lista)
    else:
        while i < (n):
            lista[i] = lista[i-1] + lista[i-2]
            i += 1
    return (lista)


        
    
    

            
        
        