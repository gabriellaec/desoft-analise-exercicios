def verifica_preco(livro, dic_cores, dic_precos):
    if livro in dic_cores:
        preco = dic_cores[livro]
        if preco in dic_precos:
            return "{0}".format(preco)