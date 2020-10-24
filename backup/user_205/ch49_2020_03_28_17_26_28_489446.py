def inverte_lista(lista):
    invertido=[]
    i = 0
    while i<len(lista):
        if i==0:
            primeiro = lista[0]
            invertido.insert(-1,primeiro)
        else:
            invertido.append(lista[-i])
        i+=1
    return invertido
    
      
        
    
    
        