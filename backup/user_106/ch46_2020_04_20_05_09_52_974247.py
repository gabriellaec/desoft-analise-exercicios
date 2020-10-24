def numero_no_indice(lista):
    iguais=[]
    for i in lista:
        if lista[i]==i:
            iguais.append(i)
    return iguais