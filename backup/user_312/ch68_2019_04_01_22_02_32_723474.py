def separa_trios(lista):
    lista_pivot=[]
    lista_final=[]
    contador=0
    contador2=0
    while contador<len(lista):
        if contador2<3:
            lista_pivot.append(lista[contador])
            contador+=1
            contador2+=1
        if contador==len(lista) or contador2==3:
            contador2=0
            lista_final.append(lista_pivot)
            lista_pivot=[]
    return lista_final