def estritamente_crescente(lista):
    lista_estritamente_crescente= [lista[0]]
    i= 0
    while i < len(lista):
        if lista[i-1] < lista[i]:
            lista_estritamente_crescente.append(lista[i])
        i= i + 1
  
        
        