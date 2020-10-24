def verifica_preco(titulo, dic_cores, dic_precos):
    for titulo in dic_cores.keys():
        for dic_cores[titulo] in dic_precos.keys():
            return dic_precos[dic_cores[titulo]]