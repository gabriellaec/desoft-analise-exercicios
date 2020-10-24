def verifica_preco(titulo_do_livro,nome_do_livro,preco_do_livro):
    for j in nome_do_livro: #primeiro dicionario
        if j==titulo_do_livro:
            cor_do_livro=nome_do_livro[j]
    for k in preco_do_livro: #segundo dicionario
        if k==cor_do_livro:
            total=preco_do_livro[k]
    return total
        