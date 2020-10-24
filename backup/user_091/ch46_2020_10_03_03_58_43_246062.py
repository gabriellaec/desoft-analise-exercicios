def numero_no_indice(lista):
    i=0
    lista_novo=[]
    while i<len(lista):
        if lista[i]==i:
            lista_novo.append(i)
            i+=1
        else:
            i+=1
            
    return lista_novo
    
    
            
    