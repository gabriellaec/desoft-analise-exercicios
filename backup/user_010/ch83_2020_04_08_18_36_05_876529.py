def medias_por_inicial (dic1):
    dic={}
    for nome,nota in dic1.items():
        if nome[0] not in dic:
            dic[nome[0]]=[nota]
        else:
            dic[nome[0]].append(nota)
    for inicial,notas in dic.items():
        dic[inicial]=sum(notas)/len(notas)
    return dic