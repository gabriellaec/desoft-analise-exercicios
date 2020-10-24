def verifica_preco(n, d, c):
    corvalor = list(d.values())
    titulo = list(d.keys())
    livro_nome = list(c.keys())
    v_livro = list(c.values())
    for a in range(len(titulo)):
        if n == titulo[a]:
            valor_do_nome=corvalor[a]
            break
    cor_do_livro = corvalor[a]
    for a in range(len(v_livro)):
        if valor_do_nome == livro_nome[a]:
            return v_livro[a]