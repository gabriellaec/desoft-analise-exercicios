lista_nova=[]
def numero_no_indice(lista):
    i=0
    while len(lista)>i:
        if lista[i]==i:
            lista_nova.append(lista[i])
            i+=1
        else:
            i+=1
    return lista_nova
print(lista_nova)