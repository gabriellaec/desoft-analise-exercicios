def soma_impares(numeros):
    b=0
    c=0
    lista=[]
    for i in range(len(numeros)):
        y=numeros[i]
        if y%2!=0:
            lista.append(y)
    for b in range(len(numeros)):
        x=lista[b]
        c+=x
    return c