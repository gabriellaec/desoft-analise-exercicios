lista= [0,4,7,16,8]
lista_estritamente_crescente= [lista[0]]
def estritamente_crescente(lista):
    i= 1
    while i < len(lista):
        if lista[i-1] < lista[i]:
            lista_estritamente_crescente.append(lista[i])
        i= i + 1
  
        
        