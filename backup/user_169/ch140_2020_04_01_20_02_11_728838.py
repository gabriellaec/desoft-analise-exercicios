def faixa_notas(lista):
    notab=0
    m=0
    notaa=0
    
    while lista[i]<len(lista):
        if lista[i]<5:
            notab+=1
        
        if lista[i]<=7 and lista[i]>=5:
            m+=1
        else:
            notaa+=1
    
    lista2=[notab,m,notaa]
    return lista2
    
    
    
    
            
       
            