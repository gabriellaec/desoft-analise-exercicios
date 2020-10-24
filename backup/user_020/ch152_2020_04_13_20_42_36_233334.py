def verifica_preco(nome, livros, cores):
    if nome in livros:
        cor_livro = livros[nome]
    if cor_livro in cores:
        preço = cores[cor_livro]
        return preco
