def conta_ocorrencias(lista):
  
    lista2=[]
    lista3=[]
    

    for i in range(len(lista)):
        lista.count(lista[i])  
        lista3.append(  lista.count(lista[i]) ) 
      
   


    for i in lista:
        if lista.count(i)>1:
            lista.remove(i)

    for i in range(len(lista)):
        lista2.append(lista[i])
        
    list(zip(lista2,lista3))

    dict(zip(lista2,lista3))
       
    
   
    return dict(zip(lista2,lista3))
        
    