def estritamente_crescente(lista_numeros):
lista_nova = []
lista_nova.append(lista_numeros[0])
i = 0
j = 1

    while j < len(lista_numeros):
        
        if lista_numeros[j] > lista_nova[i]:
            lista_nova.append(lista_numeros[j])
            i+=1
            j+=1
        
        elif lista_numeros[j] <= lista_nova[i]:
            i=i
            j+=1
    
    return  lista_nova