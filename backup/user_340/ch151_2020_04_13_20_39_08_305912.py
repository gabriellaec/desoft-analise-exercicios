def classifica_lista(lista):
    if len(lista)<2:
        return 'nenhum'
    listaC=[]*len(lista)
    listaD=[]*len(lista)
    listaC[0]=lista[0]
    listaD[0]=lista[0]
    for t in range(1,len(lista)):
        if lista[t]>listaC[t-1]:
            listaC.append(lista[t])
        if lista[t]<lista[t-1]:
            listaD.append(lista[t])
    if lista==listaC:
        return 'crescente'
    if lista==listaD:
        return 'decrescente'
    else:
        return 'nenhum'
    