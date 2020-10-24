def estritamente_crescente(lista):
    lista_crescente = []
    
    for i in range(0,len(lista)):

        if i == 0:
            lista_crescente.append(lista[i])
        
        elif lista[i] > lista[i-1]:
            lista_crescente.append(lista[i])



                                   
                                   
    return lista_crescente
