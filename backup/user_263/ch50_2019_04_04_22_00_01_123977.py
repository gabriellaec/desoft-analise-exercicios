def numero_no _indice(lista):
    iguais=[]
    indice=0
    while indice<len(lista):
        if indice==lista[indice]:
            iguais.append(indice)
        indice+=1
    return iguais