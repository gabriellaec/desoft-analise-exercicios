def  lista_primos(n):
    if n==1:
        return [2]
    else:
        lista=[]
        for i in range(3, n-1, 2):
            lista.append(n)
    return lista
            
       
        
        