def soma_valores(lista_numeros):
    contador=0
    soma=0
    while contador< len(lista_numeros):
        soma+= lista_numeros[contador]
        contador+=1
    return soma