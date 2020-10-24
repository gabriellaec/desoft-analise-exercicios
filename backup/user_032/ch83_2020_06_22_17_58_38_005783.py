def medias_por_inicial(dicionario):
    dic = {}
    for nome,nota in dicionario.items():
        i=1
        inicial = nome[0]
        if inicial not in dic:
            dic[inicial] = [nota]
        else:
            i+=1
            dic[inicial].append(nota)
    for name, grade in dic.items():
        x = 0
        for s in grade:
            x += s
        dic[name] = x/len(grade)
    return dic