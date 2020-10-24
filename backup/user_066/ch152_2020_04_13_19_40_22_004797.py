def verifica_preco(nome,livros, precos):
    if nome in livros:
        cor = livros.value(nome)
        preco_livro = preco.value(cor)
        return preco_livro