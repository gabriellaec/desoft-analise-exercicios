def verifica_preco(livro, nomelivros, dicionarioprecos):
    if livro in nomelivros:
        cor = nomelivros[livro]
        if cor in dicionarioprecos:
            valor = dicionarioprecos[cor]
            return valor