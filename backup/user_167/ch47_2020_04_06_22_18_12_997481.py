def estritamente_crescente (lista):
    i=1
    m=lista[0]
    nv=[m]
    while i < len(lista):
        i+=1
        if lista[i] < lista[i+1]:
            nv.append(lista[i+1])
        return (nv)
  
        
         
        
        
        