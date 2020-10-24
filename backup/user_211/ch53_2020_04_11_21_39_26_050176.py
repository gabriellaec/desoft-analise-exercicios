def soma_impares(lista):
    listaimpar=[]
    for i in lista:
        if i%2!=0:
            listaimpar.append(i)
    return sum(listaimpar)