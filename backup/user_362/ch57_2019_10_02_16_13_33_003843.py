def soma_impares(lista):
    lista_impares=[]
    lista_pares=[]
    contador=0
    soma=0
    while contador < len(lista):
        if lista[contador] % 2 == 0:
            lista_pares.append(contador)
        else:
            lista_impares.append(contador)
        soma=soma+lista_impares[contador]
    return soma
            