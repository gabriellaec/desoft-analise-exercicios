def verifica_preco(titulo,dic_c,dic_nome):
    if titulo in dic_nome:
        cor = dic_nome[titulo]
        if cor in dic_c:
            preco = dic_c[cor]
    return preco