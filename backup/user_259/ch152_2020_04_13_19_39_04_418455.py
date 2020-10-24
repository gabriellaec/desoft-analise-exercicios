def verifica_preco(titulo, nome_cor, cor_preco):
    for livro in nome_cor:
        if livro == titulo:
            preco = cor_preco[nome_cor[livro]]
    return preco
    