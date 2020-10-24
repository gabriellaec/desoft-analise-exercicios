def verifica_preco(nome_livro,nome,valor):
    for n in nome:
        if n==nome_livro:
            cor= nome[n]
    for v in valor:
        if v==cor:
            preco=valor[v]
    return preco