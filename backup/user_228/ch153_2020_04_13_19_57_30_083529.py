def agrupa_por_idade(dic):
    dic2={}
    for k,v in dic.values():
        if v<12:
            a='criança'
            k=nome1
            dic2[a]=nome1
        elif v<18:
            b='adolescente'
            k=nome2
            dic2[b]=nome2
        elif v<60:
            c='adulto'
            k=nome3
            dic2[c]=nome3
        else:
            d='idoso'
            k=nome4
            dic2[d]=nome4
    return dic2
        