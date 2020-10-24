lista_final=[]
def subtracao_de_lista (lista1, lista2):
    i=0
    while i < len(lista1) and i < len(lista2):
        if lista1[i] != lista2[i]:
            lista_final.append(lista1)
        i+=1
    return lista_final