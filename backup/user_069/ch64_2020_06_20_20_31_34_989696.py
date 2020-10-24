def acha_bigramas(string):

    bigramas = []

    for i in range(len(string) - 1):
        bigrama = string[i] + string[i+1]

        if not bigrama in bigramas:
            bigramas.append(bigrama)

    return bigramas