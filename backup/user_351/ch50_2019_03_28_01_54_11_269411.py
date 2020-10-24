lista = []
lista_nova= []
def numero_no_indice(lista):
    i = 0
    while i <len(lista):
        if i == lista[i]:
            lista_nova.append(lista[i])
            i+=1
        else:
            i+=1
    return lista_nova
print (numero_no_indice(lista))
        
   
    