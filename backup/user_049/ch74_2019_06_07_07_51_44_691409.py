def conta_bigramas(string):
    dict = {}
    indice = 0
    cont = 0
    for i in string:
        if not i in dict:
            dict[i] = indice
            cont+=1
        indice+=1
    return dict