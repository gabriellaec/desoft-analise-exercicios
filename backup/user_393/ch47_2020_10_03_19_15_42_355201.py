def estritamente_crescente(lista):
    lista_estritamente_crescente= []
    i= 0
    while i < len(lista):
        if lista[i] < lista[i+1]:
            lista_estritamente_crescente.append(lista[i+1])
        i= i + 1
  
        
        