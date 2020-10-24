def soma_valores(): 
    lista = [1,2,3,4]
    soma = 0 
    i = 0
    while i < len(lista):
        soma = lista[i] + soma
        i = i + 1
    return soma
