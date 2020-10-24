def verifica_preco (nome, dic):
    dic_c = {"vermelho": 10.0, "azul": 20.0, "amarelo": 40.0, "verde": 100.0 }
    if nome in dic.keys():
        v = dic[nome] 
        if v in dic_c.keys():
            return dic_c[v]