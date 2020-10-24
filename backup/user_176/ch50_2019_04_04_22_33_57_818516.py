def numero_no_indice(lista):
    lista_2=[]
    i=0
    while i<len(lista):
        if i == lista[i]:
            lista_2.append(i)
        i+=1
        return lista_2