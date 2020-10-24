def encontra_maximo(lista1, lista2, lista3):
    lista_final=[]
    lista_final.append(lista1)
    lista_final.append(lista2)
    lista_final.append(lista3)
    i=0
    p=-1
    while i<len(lista_final):
        if lista_final[i]>p:
            p=lista_final[i]
        i+=1
    return p