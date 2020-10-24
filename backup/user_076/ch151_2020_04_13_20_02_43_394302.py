def classifica_lista(lista):
    i= 0
    crescente = False
    decrescente = False
    while i+1<len(lista):
        if lista[i]<lista[i+1]:
            crescente = True
        if lista[i]>lista[i+1]:
            decrescente = True
        i+=1
    if crescente == True and decrescente == False:
        return 'crescente'
    if crescente == False and decrescente == True:
        return 'decrescente'
    if crescente == True and decrescente == True:
        return 'nenhum'