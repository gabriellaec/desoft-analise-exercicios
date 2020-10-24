def verifica_preco(livro,dic_cor,dic_preco):
    cor = 'nenhuma'
    for k,v in dic_cor.items():
        if k == livro:
            cor = v
    for k,v in dic_preco.items():
        if k == cor:
            return v