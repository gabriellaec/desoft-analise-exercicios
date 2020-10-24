def verifica_preco (nome, dic, dic_c):
    if nome in dic.keys():
        v = dic[nome] 
        if v in dic_c.keys():
            return dic_c[v]