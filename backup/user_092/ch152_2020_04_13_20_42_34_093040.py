def verifica_preco(titulo_do_livro,nomes_dos_livros,cores_dos_livros):
    if titulo_do_livro in nomes_dos_livros:
        cor_de_preco = cores_dos_livros[titulo_do_livro]
        if cor_de_preco in cores_dos_livros:
            valor_do_livro = cores_dos_livros[cor_de_preco]
            return valor_do_livro