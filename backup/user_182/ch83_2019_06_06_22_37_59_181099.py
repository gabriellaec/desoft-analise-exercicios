dicionariomedias= {'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}

def medias_por_inicial(dic):
    novodic = {}
    dicfinal = {}
    for x, v in dic.items():
        inicial = x[0]
        if inicial not in novodic.keys():
            novodic[inicial]=[v]
        else:
            novodic[inicial].append(v)
    print(novodic)
    for e in novodic:
        valores = novodic[e]
        i=0
        soma = 0
        while i<len(valores):
            soma+=valores[i]
            i+=1
        media = soma/i
        dicfinal[e]=media
    return dicfinal

print(medias_por_inicial(dicionariomedias))