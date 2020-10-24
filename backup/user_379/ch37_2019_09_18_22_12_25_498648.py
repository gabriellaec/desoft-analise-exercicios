def lista_primos(n):
    lista=[]
    i=1
    j=1
    while len(lista)<n:
        j=i
        while j>1:
            if i%j == 0 and i!=j:
                break
            else:
                j-=1
            i+=1
        if j == 1:
            lista.append(i)
    return lista
        
		
    
    