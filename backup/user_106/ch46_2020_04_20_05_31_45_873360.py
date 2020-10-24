def numero_no_indice(lista):
    iguais=[]
    for i in range(0,len(lista)):
        if i==lista[i]:
            iguais.append(i)
    return iguais