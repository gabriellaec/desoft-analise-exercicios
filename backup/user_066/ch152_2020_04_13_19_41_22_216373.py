def verifica_preco(nome,livros, precos):
    if nome in livros:
        cor = livros.get(nome)
        preco_livro = preco.get(cor)
        return preco_livro