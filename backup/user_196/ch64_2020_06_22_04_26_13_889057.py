def acha_bigramas(string):
    listabigramas = []
    for i in range(len(string)-1):
        soma = string[i] +string[i-1]
        listabigramas.append(soma)
    return listabigramas
        