lista= [0,4,7,16,8]
lista_estritamente_crescente= [lista[0]]
def estritamente_crescente(lista):
    i= 1
    while True:
        lista[i] < lista[i+1]
        lista_estritamente_crescente.append(lista[i+1])
        i= i + 1
        
        
        