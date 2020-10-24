def traduz(lista,dic):
    traducao = []
    for i in range(0,len(lista)):
        for k,v in dic.items():
            if k == lista[i]:
                traducao.append(v)
    return traducao