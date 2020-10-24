def  lista_primos(n):
    if n==1:
        return [2]
    else:
        lista=[2]
        for i in range(3, n, 2):
            lista.append(n)
    return lista
            
       
        
        