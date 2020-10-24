def soma_impares(lista):
    i=0
    liste=[]
    while i<len(lista):
        x=lista[i]%2
        if x!=int(x):
            pass
        else:
            liste.append(lista[i])
            i+=1
        return liste