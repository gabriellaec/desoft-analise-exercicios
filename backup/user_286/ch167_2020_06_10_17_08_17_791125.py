def bairro_mais_custoso(dic):
    novo_dic = {}

    for bairro in dic:
        novo_dic[bairro] = sum(dic[bairro][6:12])

    maximo = max(novo_dic.values())

    for bairro, soma in novo_dic.items():
        if soma == maximo:
            return bairro