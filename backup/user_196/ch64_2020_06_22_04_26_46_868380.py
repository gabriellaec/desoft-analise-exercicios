def acha_bigramas(string):
    listabigramas = []
    for i in range(1,len(string)-1):
        soma = string[i] +string[i-1]
        listabigramas.append(soma)
    return listabigramas
        