def estritamente_crescente (lista):
    i=1
    m=lista[0]

    novalista=[m]
    while i <= len(lista):
        if m<lista[i]:
            m=lista[i]
            novalista.append(i)
        i+=1 


        
         
        
        
        