def estritamente_crescente(lista1):
    i=0
    lista2=[]
  
    while(i<(len(lista1)-1)):
    
        if(lista1[i+1]> lista1[i]):
      
          lista2.append(lista1[i+1])

        i+=1  
  
    return lista2