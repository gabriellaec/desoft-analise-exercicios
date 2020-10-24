def verifica_preco(nome,livros, precos):
    if nome in livros:
        cor = livros.get(nome)
        preco_livro = precos.get(cor)
        return preco_livro