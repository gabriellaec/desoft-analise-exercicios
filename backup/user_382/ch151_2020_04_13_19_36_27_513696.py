def classifica_lista(lista):
    if len(lista) < 2:
        return 'nenhum'
    maximo = lista[0]
    minimo = lista[0]
    for i in range(len(l1)-1):
        while True:
            if lista[i+1] > maximo:
                maximo = lista[i+1]
                break
    if maximo == lista[-1]:
        return 'crescente'
    
    for i in range(len(l1)-1):
        while True:
            if lista[i+1] < minimo:
                minimo = lista[i+1]
                break
    if mininmo == lista[-1]:
        return 'decrescente'
    else:
        return 'nenhum'

    

    