def verifica_preco(titulo,dic_nome,dic_cor):
    if titulo in dic_nom:
        cor = dic_nome[titulo]
        if cor in dic_cor:
            preco = dic_cor[cor]
            return preco