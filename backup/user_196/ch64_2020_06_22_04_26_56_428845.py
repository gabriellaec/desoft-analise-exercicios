def acha_bigramas(string):
    listabigramas = []
    for i in range(1,len(string)):
        soma = string[i] +string[i-1]
        listabigramas.append(soma)
    return listabigramas
        