def verifica_lista(lista):
    lista_pares = []
    lista_impares = []
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            lista_pares.append(lista[i])
        elif lista[i] % 2 == 1:
            lista_impares.append(lista[i])
    if lista == lista_pares:
        return 'par'
    elif lista == lista_impares:
        return 'ímpar'
    else:
        return 'misturado