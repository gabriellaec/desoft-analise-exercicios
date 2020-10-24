def subtracao_de_listas (lista1, lista2):
    lista_final=[]
    i=0
    while i < len(lista2):
        if lista1[i] != lista2[i]:
            lista_final.append(lista1)
        i+=1
    return lista_final