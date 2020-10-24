def numero_no_indice(lista):
    iguais=[]
    indice=0
    while indice<len(lista):
        if indice==lista[indice]:
            iguais.append(indice)
        indice+=1
    return iguais