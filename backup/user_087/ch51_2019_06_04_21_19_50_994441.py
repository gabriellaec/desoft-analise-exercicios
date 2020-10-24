def estritamente_crescente(lista):
    lista_nova = []
    i = 0
    while i < len(lista):
        if lista[i] < lista[i+1]:
            lista_nova.append(lista[i])
            i += 1
        else:
            break

            
    
        