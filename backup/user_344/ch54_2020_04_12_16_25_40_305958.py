def calcula_fibonacci(n):
    i=0
    a= 2
    lista = []
    lista[0] = 1
    lista[1] = 1 
    while i < n:
        lista[a] = lista[a-1] + lista[a-2]
        a+=1
        i+=1
    return lista
    
        
    
    

        
    
    