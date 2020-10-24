def estritamente_crescente (lista):
    i=1
    m=lista[0]
    nv=[m]
    while i < len(lista):
       
        if m < lista[i]:
            nv.append(lista[i])
        i+=1
        return (nv)
  
        
         
        
        
        