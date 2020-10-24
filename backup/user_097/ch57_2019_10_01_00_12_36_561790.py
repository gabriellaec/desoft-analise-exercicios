def soma_impares(lista):
    i = 0
    sum_impares = 0
    while (i < len(lista)):
        if(lista[i]%2!=0):
            sum_impares = sum_impares + lista[i]
        i = i + 1
    return sum_impares