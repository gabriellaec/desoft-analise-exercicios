def verifica_preço(titulo,dic_livro,dic_preço):
    if titulo in dic_livro:
        cor = dic_livro[titulo]
        if cor in dic_preco:
            preco = dic_preco[cor]
    return preco