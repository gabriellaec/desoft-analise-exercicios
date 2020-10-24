lista_ind=[]

def numero_no_indice(lista):
    num_lista=len(lista)
    i = 0
    while i < num_lista:
        if lista[i] == i:
            lista_ind.append(lista[i])
            i+=1
        else:
            i+=1