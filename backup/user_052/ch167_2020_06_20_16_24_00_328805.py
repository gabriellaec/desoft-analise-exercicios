def bairro_mais_custoso (empresa):
    novo = {}
    for bairro in empresa:
        novo[bairro] = 0
        for mes in empresa[bairro][6:]:
            novo[bairro] += mes
        lista = []
        dic = {}
        for k,v in novo.items():
            dic[v] = k
            lista.append(v)
        x = max(lista)
        for w in lista:
            if w == x:
                resultado = dic[w]
    return resultado