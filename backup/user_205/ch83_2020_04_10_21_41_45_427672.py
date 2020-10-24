def medias_por_inicial(dic):
    resultado = {}
    soma = 0
    for chaves,valores in dic.items():
        for i in range(len(chaves)):
            resultado[chaves[i]]=valores/2
    print (resultado)
    return resultado

            