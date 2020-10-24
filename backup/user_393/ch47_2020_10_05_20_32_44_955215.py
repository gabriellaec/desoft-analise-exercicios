def estritamente_crescente(lista):
    if lista== []:
        return []
    lista_estritamente_crescente= []
    lista_estritamente_crescente.append(lista[0])
    i= 0
    while i < len(lista)-1:
        if lista[i] < lista[i+1]:
            lista_estritamente_crescente.append(lista[i+1])
        i= i + 1
    return lista_estritamente_crescente
  
        
        