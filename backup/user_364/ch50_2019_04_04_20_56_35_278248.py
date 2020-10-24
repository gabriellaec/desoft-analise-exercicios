lista= [1,3,2,20,4]
lista_nova= []

def numero_no_indice(lista):
    i = 0
    for e in lista:
        if e == i:
            lista_nova.append(e)

        i+=1 
    return lista_nova
print(numero_no_indice(lista))