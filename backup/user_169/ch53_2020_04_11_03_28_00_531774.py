def soma_impares(lista):

    i=0
    lista2=[]

    while i < len(lista):
        if lista[i]%2!=0:
            lista2.append(lista[i])
        i+=1
    return sum(lista2)