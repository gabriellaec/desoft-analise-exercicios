def verifica_preco(titulo, nome_cor, cor_preco):
    if titulo in nome_cor:
        cor = nome_cor[titulo]
    if cor in cor_preco:
        preco = cor_preco[cor]
        return preco
