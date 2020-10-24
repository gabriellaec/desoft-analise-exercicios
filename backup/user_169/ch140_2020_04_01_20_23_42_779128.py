def faixa_notas(lista):
    notab=0
    m=0
    notaa=0
   
    
    for i in lista:
        if  i<5:
            notab+=1
        
        elif i<=7 :
            m+=1
        
        else:
            notaa+=1
        
    lista2=[notab,m,notaa]
    return lista2
        
  
        
    
   
    
    
    
            
       
            