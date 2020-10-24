def classifica_lista(numeros):
    if len(numeros) < 2:
        return "nenhum"
    lista1 = numeros[0]
    lista2 = numeros[0]
    for i in range(len(numeros)-1):
        if lista[i+1] > lista1:
            lista1 = lista[i+1]
        elif lista[i+1] < lista2:
            lista2 = lista[i+1]
            
    if lista1 == lista[-1]:
        return "crescente"
    elif lista2 == lista[-1]:
        return "decrescente"
    else:
        return "nenhum"