def numero_no_indice(lista_num):
    lista=[]
    i=0
    while i<len(lista_num):
        for k in lista_num:
            if i==k:
                lista.append(i)
            i+=1
    return lista