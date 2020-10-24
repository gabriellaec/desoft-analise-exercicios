def verifica_preco(a, b, c):
    cor_valor=list(b.values())
    nomes=list(b.keys())
    livro=list(c.keys())
    valor=list(c.values())
    for i in range(len(nomes)):
        if a==nomes[i]:
            nome=cor_valor[i]
            break
    cor_do_livro=cor_valor[i]
    for i in range(len(valor)):
        if nome==livro[i]:
            return valor[i]