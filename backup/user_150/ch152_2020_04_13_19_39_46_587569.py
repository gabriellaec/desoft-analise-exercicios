def verifica_preco(titulo, dic_cores, dic_precos):
    for titulo in dic_cores:
        for dic_cores[titulo] in dic_precos:
            return dic_precos[dic_cores[titulo]]