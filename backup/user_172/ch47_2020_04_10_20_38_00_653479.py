def estritamente_crescente (lista):
    lista2 = []
    i = 0
    x = 1
    lista2.append(lista[0])        
    while i+x<len(lista):        
        if lista[i+x]>lista[i]:        
            lista2.append(lista[i+x])
            i+=1
        else:
            y = True
            while y:
                x+=1
                if lista[i+x]>lista[i]:
                    lista2.append(lista[i+x])
                else: 
                    y = False
            
        
    print (lista2)
    return lista2