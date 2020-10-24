def separa_trios(lista):
    lista_final=[]
    contador=0
    contador1=0
    contador2=0
    while contador<len(lista):
        lista_final[contador2].append(lista[contador])
        if contador1==2:
            contador1=0
            contador2+=1
        contador1+=1
        contador+=1
    return lista