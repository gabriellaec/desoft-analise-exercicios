def calcula_fibonacci(n):
    lista=[]
    i=0
    while i < n:
        if i==0:
            lista[i]=1
        if i==1:
            lista[i]=1
        else:    
        	lista.append(lista[i-1]+lista[i-2])
        i+=1
   
    return lista  
