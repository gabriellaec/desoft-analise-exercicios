def soma_impares(lista):
    lista_impares= []
    i= 0
    while i < len(lista):
        if lista[i]%2 != 0:
            lista_impares.append(lista[i])
        i= i + 1
    x= 0
    soma_dos_impares= 0
    while x < len(lista_impares):
        soma_dos_impares= soma_dos_impares + lista_impares[x]
        x= x + 1
    return soma_dos_impares