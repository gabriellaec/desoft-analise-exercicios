def agrupa_por_idade(dic):
    dic2={}
    for k,v in dic.values():
        if v<12:
            a='criança'
            dic2[a]=k
        elif v<18:
            b='adolescente'
            dic2[b]=k
        elif v<60:
            c='adulto'
            dic2[c]=k
        else:
            d='idoso'
            dic2[d]=k
    return dic2
        