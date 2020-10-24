
def numero_no_indice(lista):
    lista_vazia=[]
    i=0
    while i < len(lista):
        if lista[i] == i:
            lista_vazia.append(lista[i])
    return lista_vazia