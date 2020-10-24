def acha_bigramas(string):
    listabigramas = []
    for i in range(1,len(string),2):
        soma = string[i] + string[i-1]
        if soma not in listabigramas:
            listabigramas.append(soma)
    return listabigramas
        