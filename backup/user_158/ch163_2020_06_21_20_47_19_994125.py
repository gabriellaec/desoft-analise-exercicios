def calcula_media(lista):
    j=0
    for i in range(0,len(lista)):
        for nome in lista[i]:
            soma += lista[i][nome][0]
            j+=1
    media = soma/j
    return media