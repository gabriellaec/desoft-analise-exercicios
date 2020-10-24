def conta_bigramas(string):
    bigramas = []
    cont = 1
    while cont < len(string):
        bigramas.append(string[cont - 1] + string[cont])
        cont += 1
    dic = {valor: bigramas.count(valor) for valor in bigramas}
    return dic