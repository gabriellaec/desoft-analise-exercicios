def conta_bigramas(frase):
    frase.replace(' ', '')
    dic_bigramas ={}
    i = 0
    while i < len(frase) - 1:
        bigrama = str(frase[i] + frase[i + 1])
        if bigrama not in dic_bigramas.keys():
            dic_bigramas[bigrama] = 1
        else:
            for big, valor in dic_bigramas.items():
                if big == bigrama:
                    dic_bigramas[bigrama] += 1

        i += 1

    return dic_bigramas

a = 'banana nanica'