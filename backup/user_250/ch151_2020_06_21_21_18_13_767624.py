def classifica_lista(lista):
    crescente = True
    decrescente = True
    for i in range(0,len(lista)-1):
        if lista[i] > lista[i+1]:
            crescente = False
        if lista[i] < lista[i+1]:
            decrescente = False
    if crescente == True and decrescente == False:
        return 'crescente'
    if crescente == False and decrescente == True:
        return 'decrescente'
    else:
        return 'nenhum'