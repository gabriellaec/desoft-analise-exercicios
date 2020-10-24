def numero_no_indice(lista):
    lista_vazia=[]
    i=0
    while i < len(lista):
        if i == lista[i]:
            lista_vazia.append(lista[i])
            
        i+=1
    
    return lista_vazia