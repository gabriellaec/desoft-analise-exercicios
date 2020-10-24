def conta_ocorrencias(lista):
  
    lista2=[]
    lista3=[]
    

    for i in range(len(lista)):
        lista.count(lista[i])  
        lista3.append(  lista.count(lista[i]) ) 
      
    for i in lista3:
        if lista3.count(i)>1:
            lista3.remove(i)


    for i in lista:
        if lista.count(i)>1:
            lista.remove(i)
            
    lista2.append(lista)
        
    for i in range(len(lista)):
        dicionario={lista2[i]:}      
    
        

    
       
    
    return lista3

        
    