def soma_impares(lista):
    liste=[]
    for i in lista:
        if i%2 !=0:
            liste.append(i)
    return sum(liste)
        