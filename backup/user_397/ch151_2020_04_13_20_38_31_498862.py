def classifica_lista(numeros):
    if len(numeros) < 2:
        return "nenhum"
    lista1 = numeros[0]
    lista2 = numeros[0]
    for i in range(len(numeros)-1):
        if numeros[i+1] > lista1:
            lista1 = numeros[i+1]
        elif numeros[i+1] < lista2:
            lista2 = numeros[i+1]
            
    if lista1 == numeros[-1]:
        return "crescente"
    elif lista2 == numeros[-1]:
        return "decrescente"
    else:
        return "nenhum"