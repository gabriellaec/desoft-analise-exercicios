def verifica_preco(titulo,dic_nome,dic_c):
    if titulo in dic_nome:
        cor = dic_nome[titulo]
        if cor in dic_c:
            valor_l = dic_c[cor]
    return valor_l