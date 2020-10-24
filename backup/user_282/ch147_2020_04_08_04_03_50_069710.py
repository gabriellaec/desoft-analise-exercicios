def mais_frequente(lista):
    count = dict()
    for palavra in lista:
        if palavra not in count:
            count[palavra] = 1
        else:
            count[palavra] += 1
    valores = count.values()
    for e in valores:
        return(e)