def junta_listas(lista):
    leo=[]
    lista2=[]
    i=0
    c=0
    while i<len(lista):
        lista2.append(lista[i])
        leo+=lista2[c]
        i+=1
        c+=1
        
    return leo
        
  
  