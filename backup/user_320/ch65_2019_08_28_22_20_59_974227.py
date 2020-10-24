def acha_bigramas(string):
    bigramas = []
    cont = 1
    while cont < len(string):
        if string[cont - 1] + string[cont] not in bigramas:
            bigramas.append(string[cont - 1] + string[cont])
        cont += 1
    return bigramas