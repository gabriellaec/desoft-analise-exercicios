def agrupa_por_idade(dic_idades):
    dic_a = {}
    for i in dic:
        if dic[i] <= 11:
            dic_a[criança] = i
        elif dic[i] <= 17:
            dic_a[adolescente] = i
        elif dic[i] <= 59:
            dic_a[adulto] = i
        else:
            dic_a[idoso] = i
    return dic_a
        