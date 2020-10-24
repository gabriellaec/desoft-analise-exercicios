def calcula_fibonacci(n):
    a= 2
    lista = [0]*n
    lista[0] = 1
    if n == 1:
        return lista
    elif lista == 2:
        lista[1] = 1
        return lista    
    
    while a < n:
        lista[a] = lista[a-1] + lista[a-2]
        a+=1
        
    return lista
    
        
    
    

        
    
    