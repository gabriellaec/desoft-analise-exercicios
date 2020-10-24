def soma_impares(lista):
    lista_imp=[]
    for i in range(0, len(lista)):
        if lista[i]%2!=0:
            lista_imp.append(lista[i])
    return sum(lista_imp)