def estritamente_crescente (lista):
    i=1
    m=lista[0]
    novalista=[]
    novalista.append(m)
    while i < len(lista):
        if m<lista[i]:
            m=lista[i]
            novalista.append(m)
        i+=1 
    return novalista
 
        
         
        
        
        