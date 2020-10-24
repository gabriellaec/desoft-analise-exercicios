def verifica_preco(livro, dic_cores, dic_precos):
    if livro in dic_cores:
        cor = dic_cores[livro]
        if cor in dic_precos:
            preco = dic_precos[cor]
            return preco