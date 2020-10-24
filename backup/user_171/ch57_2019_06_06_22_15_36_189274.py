def soma_impares(lista):
    lnova=[]
    for l in range(len(lista)):
        if lista[l]%2!=0:
            lnova.append(lista[l])
    total=sum(lnova)
    return total
            