def numero_no_indice(lista):
    i = 0
    lista_nova = []
    while i <len(lista):
        if i == lista[i]:
            lista_nova.append(lista[i])
        i+=1
    return lista_nova

        
   
    