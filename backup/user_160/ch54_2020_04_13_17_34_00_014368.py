def calcula_fibonacci(n):
    lista = [0]*n
    lista[0] = 1
    lista[1] = 1
    i = 2
    if n > 1:
        while i < (n):
        lista[i] = lista[i-1] + lista[i-2]
        i += 1
    elif n == "0":
        return (1)
    return (lista)

        
    
    

            
        
        