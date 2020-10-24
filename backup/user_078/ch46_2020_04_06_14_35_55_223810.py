def numero_no_indice(lista):
    iguais=[]
    for i in range(len(lista)):
        if i == lista[i]:
            iguais.append(i)
    return iguais