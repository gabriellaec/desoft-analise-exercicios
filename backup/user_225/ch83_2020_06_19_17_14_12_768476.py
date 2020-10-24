def medias_por_inicial(dic):
    novodic = {}
    soma = 0
    contador = 1
    for i in dic:
        a = i[0]
        if a  not in novodic:
            novodic[a]=dic[i]
        else:
            novodic[a]+=dic[i]
            soma = novodic[a]
            contador+=1
            media = soma/contador
            novodic[a]=media
    return novodic