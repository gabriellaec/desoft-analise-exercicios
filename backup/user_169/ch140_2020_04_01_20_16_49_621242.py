def faixa_notas(lista):
    notab=0
    m=0
    notaa=0
    i=0
    
    while lista[i]<len(lista):
        if lista[i]<5:
            notab+=1
        
        elif lista[i]<=7 :
            m+=1
        
        if lista[i]>7:
            notaa+=1
        i+=1
    lista2=[notab,m,notaa]
    return lista2
        
  
        
    
   
    
    
    
            
       
            